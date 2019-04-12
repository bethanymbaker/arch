import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import urllib.request
from bs4 import BeautifulSoup
import xgboost as xgb
from sklearn.metrics import mean_squared_error

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from bs4 import BeautifulSoup

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

boston = load_boston()
print(boston.data.shape)
print(boston.feature_names)
print(boston.DESCR)

data = pd.DataFrame(boston.data)
data.columns = boston.feature_names
data['PRICE'] = boston.target
data.info()
data.describe()

X, y = data.iloc[:, :-1], data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

xg_reg = xgb.XGBRegressor(objective='reg:linear', colsample_bytree=0.3, learning_rate=0.1,
                          max_depth=5, alpha=10, n_estimators=10)
xg_reg.fit(X_train,y_train)

preds = xg_reg.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))
print(f"RMSE: {rmse}")

params = {"objective": "reg:linear", 'colsample_bytree': 0.3, 'learning_rate': 0.1, 'max_depth': 5, 'alpha': 10}

data_dmatrix = xgb.DMatrix(data=X, label=y)
cv_results = xgb.cv(dtrain=data_dmatrix, params=params, nfold=3, num_boost_round=50, early_stopping_rounds=10,
                    metrics="rmse", as_pandas=True, seed=123)
cv_results.head()
print((cv_results["test-rmse-mean"]).tail(1))
xg_reg = xgb.train(params=params, dtrain=data_dmatrix, num_boost_round=10)

xgb.plot_tree(xg_reg,num_trees=0)
plt.rcParams['figure.figsize'] = [50, 10]
plt.show()

xgb.plot_importance(xg_reg)
plt.rcParams['figure.figsize'] = [5, 5]
plt.show()

# nltk.download('punkt')
# nltk.download('stopwords')
# sns.set()
# nltk.download_shell()

response = urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()
print(html)


soup = BeautifulSoup(html, 'html5lib')
text = soup.get_text(strip=True)
print(text)

tokens = [t for t in text.split()]
print(tokens)

clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))

freq.plot(20, cumulative=False)



# string = "The science of today is the technology of tomorrow"
# print(nltk.tokenize.word_tokenize(string))


# def capitalizer(string: str) -> str:
#     return string.upper()
# text = 'abc'
# print(capitalizer(text))

# arr = np.linspace(-5, 5, 5000)
# df = pd.Series(arr).to_frame('original')
# df['transformed'] = 1 / (1 + np.exp(-df['original']))
# df['transformed'].plot()
# plt.grid()
# plt.title('Data')
# plt.show()
