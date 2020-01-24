import os
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

imdb_dir = '/Users/bethanybaker/Downloads/aclImdb'
train_dir = os.path.join(imdb_dir, 'train')

# pos_files = [os.path.join('pos', _) for _ in os.listdir(os.path.join(train_dir, 'pos'))]
# pos_texts = []
# for textfile in pos_files:
#     full_text_file = os.path.join(train_dir, textfile)
#     with open(full_text_file, 'r') as f:
#         text = f.read().strip()
#         pos_texts.append(text)
#
# neg_files = [os.path.join('neg', _) for _ in os.listdir(os.path.join(train_dir, 'neg'))]
# neg_texts = []
# for textfile in neg_files:
#     full_text_file = os.path.join(train_dir, textfile)
#     with open(full_text_file, 'r') as f:
#         text = f.read().strip()
#         neg_texts.append(text)
#
# texts = pos_texts + neg_texts
# labels = [1] * len(pos_texts) + [0] * len(neg_texts)

labels = []
texts = []
for label_type in ['neg', 'pos']:
    dir_name = os.path.join(train_dir, label_type)
    for fname in os.listdir(dir_name):
        if fname[-4:] == '.txt':
            f = open(os.path.join(dir_name, fname))
            texts.append(f.read())
            f.close()
            if label_type == 'neg':
                labels.append(0)
            else:
                labels.append(1)

max_words = 10000
max_len = 100

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_matrix(texts)

word_index = tokenizer.word_index
data = pad_sequences(sequences, maxlen=max_len)

# df = pd.DataFrame(data=data)
#
# sns.distplot(df.sum())
# plt.grid()
#
# sns.distplot(df.sum(axis=1))
# plt.grid()

