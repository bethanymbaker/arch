import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from hashlib import sha256

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', 100)

alphabet_dicts = []
image_types = ['images_background', 'images_evaluation']
for image_type in image_types:
    path = f'/Users/bethanybaker/omniglot/python/{image_type}'
    alphabet_list = [f for f in os.listdir(path) if not f.startswith('.')]
    for alphabet in alphabet_list:
        character_list = [f for f in os.listdir(os.path.join(path, alphabet)) if not f.startswith('.')]
        for character in character_list:
            images = [f for f in os.listdir(os.path.join(path, alphabet, character)) if not f.startswith('.')]
            for image in images:
                alphabet_dicts.append({'alphabet': alphabet.lower(),
                                       'character': character,
                                       'entity_id': '_'.join([alphabet.lower(), character]),
                                       'image_path': os.path.join(path, alphabet, character, image),
                                       'type': image_type.split('_')[1]})

alphabet_df = pd.DataFrame(alphabet_dicts)

test_image_path = alphabet_df.sample().image_path.values[0]
im = plt.imread(test_image_path)

background = alphabet_df[alphabet_df.type == 'background'].drop(columns=['type', 'alphabet', 'character'])
evaluation = alphabet_df[alphabet_df.type == 'evaluation'].drop(columns=['type', 'alphabet', 'character'])

from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Lambda, BatchNormalization
from keras.models import Sequential, Model
from keras import backend as K


def siamese_model(input_shape):
    left = Input(input_shape)
    right = Input(input_shape)
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(BatchNormalization())
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(BatchNormalization())
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(BatchNormalization())
    model.add(Conv2D(256, (3, 3), activation='relu'))
    model.add(BatchNormalization())
    model.add(Conv2D(256, (3, 3), activation='relu'))
    model.add(MaxPooling2D())
    model.add(BatchNormalization())
    model.add(Flatten())
    model.add(Dense(512, activation='sigmoid'))

    left_encoded = model(left)
    right_encoded = model(right)
    l1_layer = Lambda(lambda tensors: K.abs(tensors[0] - tensors[1]))
    l1_distance = l1_layer([left_encoded, right_encoded])
    prediction = Dense(1, activation='sigmoid')(l1_distance)
    siamese_net = Model(inputs=[left, right], outputs=prediction)
    return siamese_net

# model = siamese_model((150, 150, 1))
# model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])

