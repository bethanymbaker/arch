import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.parse import urlparse
import requests
import pickle
from multiprocessing import Pool

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', 50)

pageviews = pd.read_csv("~/Desktop/data/pageviews.csv",
                        index_col=0,
                        parse_dates=[2]) \
    .rename(columns={'time': 'created_at'})
users = pd.read_csv("~/Desktop/data/users.csv",
                    index_col=0,
                    parse_dates=[2])

assert pageviews.user_id.nunique() == users.user_id.nunique()

users['created_at_date'] = pd.to_datetime(users.created_at.dt.strftime('%Y-%m-%d'))

pageviews['created_at_date'] = pd.to_datetime(pageviews.created_at.dt.strftime('%Y-%m-%d'))
pageviews['website'] = pageviews.article_url.apply(lambda url: urlparse(url).netloc)

pageviews['page_rank'] = pageviews.groupby('user_id')['created_at'].rank('first')
pageviews['total_pageviews'] = pageviews.groupby('user_id')['page_rank'].transform('max')
pageviews['visit_number'] = pageviews.groupby('user_id')['created_at_date'].rank('dense')
pageviews['first_visit_date'] = pageviews.groupby('user_id')['created_at_date'].transform('min')

pageviews['user_cohort'] = pageviews.groupby('user_id')['created_at_date'].transform('min').dt.strftime('%Y-%m-01').map(pd.to_datetime)
pageviews['is_first_page'] = pageviews.page_rank == 1
pageviews['is_first_visit'] = pageviews.visit_number == 1
pageviews['num_visits'] = pageviews.groupby('user_id')['visit_number'].transform('max')
pageviews['last_visit_date'] = pageviews.groupby('user_id')['created_at_date'].transform('max')

pageviews = pd.merge(pageviews,
                     pageviews[pageviews.page_rank == 1][['user_id', 'marketing_channel']].drop_duplicates()
                     .rename(columns={'marketing_channel': 'acquisition_channel'}),
                     on='user_id',
                     how='left')

pageviews['days_since_first_visit'] = (pageviews.created_at_date - pageviews.first_visit_date).dt.days
pageviews['customer_lifetime'] = (pageviews.last_visit_date - pageviews.first_visit_date).dt.days


pageviews['delta_t'] = (pageviews.created_at_date.max() - pageviews.created_at_date).dt.days
half_life = 30
pageviews['value'] = pageviews.delta_t.map(lambda val: 0.5**(val / half_life))
pageviews['num_title_words'] = pageviews.article_title.map(lambda title: len(title.split(' ')))


# test = pageviews[pageviews.user_id == 'ba87d67b-0b90-4693-9da0-b6ed99002d69']


from sklearn.feature_extraction.text import HashingVectorizer
vectorizer = HashingVectorizer(stop_words='english',
                               ngram_range=(1, 2),
                               strip_accents='unicode',
                               n_features=512)

df = pd.DataFrame(data=pageviews.article_title.drop_duplicates())

X = pd.DataFrame(vectorizer.fit_transform(df['article_title']).toarray())
df_2 = pd.concat([df, X], axis=1)


from sklearn.cluster import KMeans

intertias = []
for num_clusters in range(1, 25):
    print(f'num_clusters = {num_clusters}')
    kmeans = KMeans(n_clusters=num_clusters)
    res = kmeans.fit(X)
    intertias.append(res.inertia_)

plt.plot(list(range(1, 25)), intertias)
plt.grid()

########################################################################################################################
# Look at median time to next visit
tmp = pageviews[['user_id', 'visit_number', 'created_at_date']].drop_duplicates().sort_values(['user_id', 'created_at_date'])
tmp['next_visit_date'] = tmp.groupby('user_id').created_at_date.shift(-1)
tmp['days_to_next_visit'] = (tmp.next_visit_date - tmp.created_at_date).dt.days

# 30 Day Half Life ;)



# pageviews[pageviews.user_id == '10b2c9ab-c3fe-49cd-81a8-89761a5d372f']
# pageviews.groupby(['user_cohort', 'acquisition_channel'])['user_id'].nunique().unstack('acquisition_channel').plot(grid=True)


def get_retention_cohort(val):
    dayz = [0, 30, 60, 90, 120, 180, np.inf]
    for day in dayz:
        if val <= day:
            return day


pageviews['retention_cohort'] = pageviews.days_since_first_visit.map(get_retention_cohort)

df = pageviews.groupby(['user_cohort', 'retention_cohort']).user_id.nunique()
df_2 = df.unstack('retention_cohort')

cohort_sizes = df_2.loc[:, 0.0].copy()

df_3 = df_2.div(cohort_sizes.values, axis=0).drop(columns=[np.inf, 0.0])
df_3.plot(grid=True)

########################################################################################################################
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(stop_words='english', ngram_range=(1, 2), max_features=10000)
vectorizer.fit_transform(pageviews.article_title)

from keras.models import Sequential
from keras.layers import Flatten, Dense, Embedding

from keras.datasets import imdb
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical


vocab_size = 10000
max_length = 20

tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(pageviews.article_title)
sequences = tokenizer.texts_to_sequences(pageviews.article_title)

word_index = tokenizer.word_index
print(f'found {len(word_index)} unique tokens')
data = pad_sequences(sequences, max_length)

X = pd.DataFrame(data=data)
y = pageviews[['website']].copy()
y['website_cat'] = y.website.astype('category').cat.codes.astype(str)
y.set_index('website', inplace=True)
# y = pd.get_dummies(y)
y = to_categorical(y.website_cat)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)


model = Sequential()
model.add(Embedding(vocab_size, 8, input_length=max_length))
model.add(Flatten())
model.add(Dense(pageviews.website.nunique(), activation='sigmoid'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

print(model.summary())

history = model.fit(X_train, y_train, epochs=20, verbose=10, batch_size=512, validation_data=(X_test, y_test))

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(loss) + 1)
import matplotlib.pyplot as plt
plt.plot(epochs, loss, 'bo', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

acc = history.history['acc']
val_acc = history.history['val_acc']

epochs = range(1, len(loss) + 1)
import matplotlib.pyplot as plt
plt.plot(epochs, acc, 'bo', label='Training Loss')
plt.plot(epochs, val_acc, 'b', label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

########################################################################################################################
model = Sequential()
model.add(Embedding(10000, 8, input_length=max_length))
model.add(Flatten())
model.add(Dense(pageviews.website.nunique(), activation='softmax'))

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['acc'])
model.summary()

history = model.fit(X_train, y_train,
                    epochs=10,
                    batch_size=32,
                    validation_split=0.2)

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=vocab_size)
x_train = pad_sequences(x_train, maxlen=max_length)
x_test = pad_sequences(x_test, maxlen=max_length)

# model = Sequential()
# model.add(Embedding(10000, 8, input_length=maxlen))
# model.add(Flatten())
# model.add(Dense(1, activation='sigmoid'))
# model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
# model.summary()
#
# history = model.fit(x_train, y_train,
#                     epochs=10,
#                     batch_size=32,
#                     validation_split=0.2)

########################################################################################################################

# def get_data(url):
#     global aa
#     print(f'count = {aa.value}')
#     aa += 1
#     try:
#         r = requests.get(url, timeout=5)
#         if r.status_code == 200:
#             return url, r.status_code, requests.get(url, timeout=5).text
#         else:
#             return url, r.status_code
#     except:
#         return url
#
#
# df = pd.DataFrame(data=pageviews.article_url.unique(), columns=['article_url'])
# df_2 = df.sample(10).copy()
#
# # Initialise pool of workers.
# with Pool(4) as p:
#     res = p.map(get_data, df_2['article_url'].values)


# with open('pageviews.dat', 'rb') as f:
#     pickle.dump(pageviews, f)
#
# # users.isna().sum()
# # Out[4]:
# # user_id                0
# # created_at             0
# # job_function       10754
# # job_industry       10837
# # use_case            9919
# # created_at_date        0
# # dtype: int64
# #
# # users.nunique()
# # Out[8]:
# # user_id            12461
# # created_at         12461
# # job_function          10
# # job_industry          32
# # use_case               8
# # created_at_date      232
# # dtype: int64
# #
# # users.job_function.value_counts(normalize=True).plot(kind='bar', grid=True)
# # plt.xticks(rotation='45', ha='right')
# # plt.title('Job Functions')
# # plt.gcf().tight_layout()
# #
# # users.job_industry.value_counts(normalize=True).plot(kind='bar', grid=True)
# # plt.xticks(rotation='45', ha='right')
# # plt.title('Job Industry')
# # plt.gcf().tight_layout()
# #
# # users.use_case.value_counts(normalize=True).plot(kind='bar', grid=True)
# # plt.xticks(rotation='45', ha='right')
# # plt.title('Use Case')
# # plt.gcf().tight_layout()
#
# # Some featurization
#
#
# # Some EDA

users.groupby('created_at_date').user_id.nunique().plot(grid=True)
plt.title('User Ids Created By Date')
plt.gcf().tight_layout()

sns.distplot(pageviews.groupby('user_id').size())
plt.grid()
plt.title('Number of PageViews Per User Id')

sns.distplot(pageviews.groupby('user_id').size()[pageviews.groupby('user_id').size() <= 25])
plt.grid()
plt.title('Number of PageViews Per User Id')

pageviews.groupby('user_id').size().value_counts(normalize=True).head(10).plot(kind='bar', grid=True)

pageviews.groupby('user_id').size().to_frame('Num Pageviews').boxplot()
plt.title('Boxplot of Pageviews Per User')

pageviews.marketing_channel.value_counts()
