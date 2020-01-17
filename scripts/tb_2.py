import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
from new_class import LinearRegression

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 200)


interests = pd.read_csv('~/Desktop/interview_data_062019/company_candidate_interests.csv')
data = pd.read_csv('~/Desktop/interview_data_062019/interview_data.csv')

good_feat = [
    "experience_and_interests__years_xp",
    "main_criterias__algorithmic_knowledge",
    "main_criterias__architecture_skill",
    "main_criterias__back_end_web_understanding",
    "main_criterias__coding_productivity",
    "main_criterias__culture_fit_and_friendliness",
    "main_criterias__low_level_systems_understanding",
    "main_criterias__placeability",
    "main_criterias__professional_code",
    "main_criterias__technical_communication",
    "quiz_score",
    "interviewer_decision"
]
X = data[good_feat + ['candidate_id']].copy().set_index('candidate_id')

X.loc[X.main_criterias__back_end_web_understanding.isna(), 'main_criterias__back_end_web_understanding'] = X.main_criterias__back_end_web_understanding.mean()
X.loc[X.main_criterias__low_level_systems_understanding.isna(), 'main_criterias__low_level_systems_understanding'] = X.main_criterias__low_level_systems_understanding.mean()
X.loc[X.experience_and_interests__years_xp.isna(), 'experience_and_interests__years_xp'] = X.experience_and_interests__years_xp.mean()


X = pd.get_dummies(X, drop_first=True).sort_index()

y = interests.groupby('candidate_id').size().to_frame()
y.columns = ['num_hits']

XX = pd.merge(X, y, left_index=True, right_index=True)
X = XX.drop(columns=['num_hits'])
y = XX[['num_hits']].copy()

# scoring = ['explained_variance', 'r2', 'neg_median_absolute_error', 'neg_mean_squared_error']
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y)

model = XGBRegressor(objective='reg:squarederror')
model.fit(X_train, y_train)

new_df = pd.DataFrame(index=X_train.columns)
new_df['importance'] = model.feature_importances_
new_df = new_df.sort_values('importance', ascending=False)
new_df.plot(kind='bar', grid=True)
plt.xticks(rotation='45', ha='right')
plt.tight_layout()

y_test.loc[:, 'y_pred_num'] = model.predict(X_test)

print(f'r2_score = {metrics.r2_score(y_test.num_hits, y_test.y_pred_num)}')
print(f'mean_squared_error = {metrics.mean_squared_error(y_test.num_hits, y_test.y_pred_num)}')

# from sklearn.linear_model import LinearRegression

vals = 10.**np.arange(-4, 3, 0.1)
res = pd.DataFrame(index=vals, columns=['r2', 'mse'])

for l2_reg in vals:
    lin_model = LinearRegression(fit_intercept=True, l2_reg=l2_reg)
    lin_model.fit(X_train.values, y_train.values)

    y_test['y_pred_lm'] = lin_model.predict(X_test.values).reshape(-1, 1)
    res.loc[l2_reg, 'r2'] = metrics.r2_score(y_test.num_hits, y_test.y_pred_lm)
    res.loc[l2_reg, 'mse'] = metrics.mean_squared_error(y_test.num_hits, y_test.y_pred_lm)

    # print(f'r2_score = {metrics.r2_score(y_test.num_hits, y_test.y_pred_lm)}')
    # print(f'mean_squared_error = {metrics.mean_squared_error(y_test.num_hits, y_test.y_pred_lm)}')

y_test.plot(kind='scatter', x='num_hits', y='y_pred_num')
ax = res.plot(subplots=True, grid=True)
ax[0].set_xscale('log')
