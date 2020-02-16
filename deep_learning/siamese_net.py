import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

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
                alphabet_dicts.append({'alphabet': alphabet,
                                       'character': character,
                                       'image_path': os.path.join(path, alphabet, character, image),
                                       'type': image_type.split('_')[1]})

alphabet_df = pd.DataFrame(alphabet_dicts)

test_image_path = alphabet_df.sample().image_path.values[0]
im = plt.imread(test_image_path)