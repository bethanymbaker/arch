from keras.datasets import imdb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

sett = set()
for lst in train_data:
    for elem in lst:
        sett.add(elem)


# train_data_string = [type(list_of_int) for list_of_int in train_data]
# train_data_string = [[str(i) for i in list_of_int] for list_of_int in train_data]

tmp = pd.DataFrame(data=train_data, columns=['int_list'])
tmp['str_list'] = tmp.int_list.map(lambda lst: [str(i).rjust(2, '0') for i in lst])
tmp['text'] = tmp.str_list.map(lambda lst: ' '.join(lst))

vectorizer = CountVectorizer()
vectorizer.fit_transform(tmp['text'])


X_train = pd.DataFrame(data=train_data)
y_train = pd.DataFrame(data=train_labels, columns=['label'])