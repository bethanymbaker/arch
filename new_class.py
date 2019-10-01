from sklearn.datasets import make_regression
import pandas as pd
import numpy as np


class LinearRegression:

    def __init__(self, fit_intercept=False, l2_reg=0):
        self.betas = None
        self.fit_intercept = fit_intercept
        self.l2_reg = l2_reg

    def fit(self, X, y):
        if self.fit_intercept:
            X = self.add_column(X)
        A = np.matmul(X.T, X) + self.l2_reg * np.eye(X.shape[1])
        A_inv = np.linalg.inv(A)
        betas = np.matmul(A_inv, np.matmul(X.T, y))
        self.betas = betas

    def predict(self, X):
        if self.fit_intercept:
            X = self.add_column(X)
        return np.matmul(X, self.betas)

    def score(self, X, y):
        preds = self.predict(X)
        return np.mean((preds - y)**2)

    def add_column(self, X):
        xx = pd.DataFrame(X)
        xx['extra_col'] = 1
        return xx.values


if __name__ == '__main__':
    X, y, true_coef = make_regression(n_samples=5000, n_features=1000, coef=True, bias=10)

    lr = LinearRegression(fit_intercept=True)
    lr.fit(X, y)
    pred = lr.predict(X)
    print(f'mse = {lr.score(X, y)}')
    no_reg = lr.betas

    lr = LinearRegression(fit_intercept=True, l2_reg=1000)
    lr.fit(X, y)
    pred = lr.predict(X)
    print(f'mse = {lr.score(X, y)}')
    with_reg = lr.betas

    df = pd.DataFrame(data=no_reg, columns=['no_reg'])
    df['reg'] = with_reg
    df.sort_values('no_reg', ascending=False, inplace=True)
    df.head(15).plot(kind='bar', grid=True)


