import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn import metrics
from sklearn.metrics import f1_score, roc_auc_score
from xgboost import XGBClassifier

from imblearn.over_sampling import SMOTE
from imblearn.metrics import classification_report_imbalanced

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 150)

# Origination wrangling
origination_data_file = "~/Desktop/historical_data1_2009/historical_data1_Q12009/historical_data1_Q12009.txt"
origination_names = ["fico",
                     "first_payment_date",
                     "is_first_time_home_buyer",
                     "maturity_date",
                     "msa",
                     "mort_ins_pct",
                     "num_units",
                     "occpy_sts",
                     "cltv",
                     "dti",
                     "orig_upb",
                     "ltv",
                     "interest_rate",
                     "channel",
                     "is_ppmt_pnlty",
                     "prod_type",
                     "state",
                     "prop_type",
                     "zipcode",
                     "id_loan",
                     "loan_purpose",
                     "orig_loan_term",
                     "num_borr",
                     "seller_name",
                     "servicer_name",
                     "is_super_conforming"]

origination = pd.read_csv(origination_data_file,
                          header=None,
                          delimiter='|',
                          names=origination_names,
                          index_col='id_loan',
                          na_values={'fico': 9999,
                                     'is_first_time_home_buyer': 9,
                                     'mort_ins_pct': 999,
                                     'num_units': 99,
                                     'occpy_sts': 9,
                                     'cltv': 999,
                                     'dti': 999,
                                     'ltv': 999,
                                     'channel': 9,
                                     'prop_type': 99,
                                     'loan_purpose': 9,
                                     'num_borr': 99})\
    .drop(columns=['first_payment_date',
                   'maturity_date',
                   'prod_type',
                   'seller_name',
                   'servicer_name'])

# Examine correlation of features
_ = origination.corr().stack().reset_index().sort_values(by=0, ascending=False)
_ = _[_[0] != 1.0]
_.head(20)
_.tail(20)
# Note that cltv and ltv are highly correlated 0.952995. I will most likely
# remove one of these feautres

numeric_features = ['fico',
                    'mort_ins_pct',
                    'num_units',
                    'cltv',
                    'dti',
                    'orig_upb',
                    'ltv',
                    'interest_rate',
                    'orig_loan_term']

# Print number of missing observations
print(origination[numeric_features].isna().sum())
# dti missing 2602 values

category_features = ['is_first_time_home_buyer',
                     'channel',
                     'is_ppmt_pnlty',
                     'prop_type',
                     'msa',
                     'occpy_sts',
                     'state',
                     'zipcode',
                     'loan_purpose',
                     'num_borr',
                     'is_super_conforming']

for col in category_features:
    new_col = origination[col].astype('category')
    if len(new_col[new_col.isna()]) > 0:
        dumm = pd.get_dummies(new_col, prefix=col, drop_first=True, dummy_na=True)
    else:
        dumm = pd.get_dummies(new_col, prefix=col, drop_first=True)
    for coll in dumm.columns:
        origination[coll] = dumm[coll]
    del origination[col]

plot_flag = False
if plot_flag:
    fig, axes = plt.subplots(3, 3, figsize=(12, 12))

    sns.distplot(origination[~origination['fico'].isna()]['fico'], ax=axes[0, 0])
    axes[0, 0].set_xlabel('fico')
    axes[0, 0].grid()

    sns.distplot(origination[~origination['mort_ins_pct'].isna() & (origination.mort_ins_pct != 0)]['mort_ins_pct'], ax=axes[0, 1])
    axes[0, 1].set_xlabel('mort_ins_pct')
    axes[0, 1].grid()

    sns.distplot(origination[~origination['cltv'].isna()]['cltv'], ax=axes[0, 2])
    axes[0, 2].set_xlabel('cltv')
    axes[0, 2].grid()

    sns.distplot(origination[~origination['dti'].isna()]['dti'], ax=axes[1, 0])
    axes[1, 0].set_xlabel('dti')
    axes[1, 0].grid()

    sns.distplot(origination[~origination['ltv'].isna()]['ltv'], ax=axes[1, 1])
    axes[1, 1].set_xlabel('ltv')
    axes[1, 1].grid()

    sns.distplot(origination[~origination['interest_rate'].isna()]['interest_rate'], ax=axes[1, 2])
    axes[1, 2].set_xlabel('interest_rate')
    axes[1, 2].grid()

    sns.distplot(origination[~origination['num_units'].isna()]['num_units'], ax=axes[2, 0])
    axes[2, 0].set_xlabel('num_units')
    axes[2, 0].grid()

    sns.distplot(origination[~origination['orig_upb'].isna()]['orig_upb'], ax=axes[2, 1])
    axes[2, 1].set_xlabel('orig_upb')
    axes[2, 1].grid()

    sns.distplot(origination[~origination['orig_loan_term'].isna()]['orig_loan_term'], ax=axes[2, 2])
    axes[2, 2].set_xlabel('orig_loan_term')
    axes[2, 2].grid()

    fig.suptitle('Distribution of numeric features')
    fig.savefig('/Users/bethanybaker/Desktop/2019-04-17_Feature-Distributions.png')
    plt.close(fig)


# Performance wrangling
monthly_performance_data_file = \
    "~/Desktop/historical_data1_2009/historical_data1_Q12009/historical_data1_time_Q12009.txt"
performance_names = ["id_loan",
                     "monthly_reporting_period",
                     "current_upb",
                     "delq_sts",
                     "loan_age",
                     "mths_remng",
                     "repch_flag",
                     "flag_mod",
                     "cd_zero_bal",
                     "dt_zero_bal",
                     "current_int_rt",
                     "non_int_brng_upb",
                     "dt_lst_pi",
                     "mi_recoveries",
                     "net_sale_proceeds",
                     "non_mi_recoveries",
                     "expenses",
                     "legal_costs",
                     "maint_pres_costs",
                     "taxes_ins_costs",
                     "misc_costs",
                     "actual_loss",
                     "modcost",
                     "stepmod_ind",
                     "dpm_ind",
                     "eltv"]
st = datetime.now()
performance = pd.read_csv(monthly_performance_data_file,
                          header=None,
                          delimiter="|",
                          names=performance_names,
                          usecols=['id_loan', 'delq_sts', 'loan_age', 'cd_zero_bal'],
                          dtype={'delq_sts': str})
print(f"time to load performance data: {datetime.now() - st}")

df_2 = performance.groupby('id_loan').tail(1)
df_3 = df_2[df_2.delq_sts != 'R'].copy()
df_3.delq_sts = df_3.delq_sts.astype(int)
df_3['is_deliquent'] = df_3.delq_sts.apply(lambda x: 1 if x >= 3 else 0)
df_3.set_index('id_loan', inplace=True)

df_4 = pd.merge(origination, df_3['is_deliquent'], left_index=True, right_index=True)











# df_ = df_4[numeric_features + ['is_deliquent']]
# _ = sns.pairplot(df_.sample(frac=0.01))
# _.savefig("/Users/bethanybaker/Desktop/numeric_features_pairplot.png")
# sns.heatmap(df_.corr())

##################
df_5 = df_4.dropna().sample(frac=0.1)

X, y = df_5.iloc[:, :-1], df_5.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Train model
clf_3 = SVC(class_weight='balanced', probability=True)

clf_3.fit(X_train, y_train)

# Predict on training set
pred_y_3 = clf_3.predict(X_test)

# Is our model still predicting just one class?
print(np.unique(pred_y_3))
# [0 1]

# How's our accuracy?
print(accuracy_score(y_test, pred_y_3))
# 0.688

# What about AUROC?
prob_y_3 = clf_3.predict_proba(X_test)
prob_y_3 = [p[1] for p in prob_y_3]
print(roc_auc_score(y_test, prob_y_3))

# Train model
clf_4 = RandomForestClassifier()
clf_4.fit(X_train, y_train)

# Predict on training set
pred_y_4 = clf_4.predict(X_test)

# Is our model still predicting just one class?
print(np.unique(pred_y_4))

# How's our accuracy?
print(accuracy_score(y_test, pred_y_4))

# What about AUROC?
prob_y_4 = clf_4.predict_proba(X_test)
prob_y_4 = [p[1] for p in prob_y_4]
print(roc_auc_score(y_test, prob_y_4))


alg = XGBClassifier(learning_rate=0.1,
                    n_estimators=140,
                    max_depth=5,
                    min_child_weight=3,
                    gamma=0.2,
                    subsample=0.6,
                    colsample_bytree=1.0,
                    objective='binary:logistic',
                    nthread=4,
                    scale_pos_weight=1,
                    seed=27)
alg.fit(X_train, y_train, eval_metric='auc')

predictions = alg.predict(X_test)
pred_proba = alg.predict_proba(X_test)[:, 1]

print("Accuracy Score : %.4g" % metrics.accuracy_score(y_test, predictions))
print("AUC: %f" % metrics.roc_auc_score(y_test, pred_proba))
print("F1 Score: %f" % metrics.f1_score(y_test, predictions))

feat_imp = alg.feature_importances_
feat = X_train.columns.tolist()
res_df = pd.DataFrame({'Features': feat, 'Importance': feat_imp}).sort_values(by='Importance', ascending=False)
res_df.plot('Features', 'Importance', kind='bar', title='Feature Importances')
plt.ylabel('Feature Importance Score')
plt.show()
print(res_df)
print(res_df["Features"].tolist())
