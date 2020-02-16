import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', 100)

images_background_path = '/Users/bethanybaker/omniglot/python/images_background'
images_evaluation_path = '/Users/bethanybaker/omniglot/python/images_evaluation'
alphabet_dicts = []

alphabet_list = [f for f in os.listdir(images_background_path) if not f.startswith('.')]
for alphabet in alphabet_list:
    character_list = [f for f in os.listdir(os.path.join(images_background_path, alphabet)) if not f.startswith('.')]
    for character in character_list:
        images = [f for f in os.listdir(os.path.join(images_background_path, alphabet, character)) if not f.startswith('.')]
        for image in images:
            alphabet_dicts.append({'alphabet': alphabet,
                                   'character': character,
                                   'image_path': os.path.join(images_background_path, alphabet, character, image),
                                   'type': 'background'})

alphabet_list = [f for f in os.listdir(images_evaluation_path) if not f.startswith('.')]
for alphabet in alphabet_list:
    character_list = [f for f in os.listdir(os.path.join(images_evaluation_path, alphabet)) if not f.startswith('.')]
    for character in character_list:
        images = [f for f in os.listdir(os.path.join(images_evaluation_path, alphabet, character)) if not f.startswith('.')]
        for image in images:
            alphabet_dicts.append({'alphabet': alphabet,
                                   'character': character,
                                   'image_path': os.path.join(images_evaluation_path, alphabet, character, image),
                                   'type': 'evaluation'})

alphabet_df = pd.DataFrame(alphabet_dicts)

test_image_path = alphabet_df.sample().image_path.values[0]
im = plt.imread(test_image_path)