import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import f1_score, roc_auc_score, accuracy_score
from xgboost import XGBClassifier
from sklearn.feature_selection import mutual_info_classif
import numpy as np

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

# Examine correlation of numeric features
numeric_features = ['fico',
                    'mort_ins_pct',
                    'num_units',
                    'cltv',
                    'dti',
                    'orig_upb',
                    'ltv',
                    'interest_rate',
                    'orig_loan_term']

_ = origination[numeric_features].corr().stack().reset_index().sort_values(by=0, ascending=False)\
    .rename(columns={0: 'corr'})
_ = _[_.level_0 != _.level_1]
_['feature_pair'] = _[['level_0', 'level_1']].apply(lambda r: "_".join(sorted([r['level_0'], r['level_1']])), axis=1)
_ = _[['feature_pair', 'corr']].drop_duplicates()

sns.distplot(_['corr'])
plt.title('Correlation of numeric features')
plt.grid()

_.head()
# Note that cltv and ltv are highly correlated 0.952995. Will need to eliminate one

# Print number of missing observations
print(origination[numeric_features].isna().sum())
# cltv                33
# dti               2602
# ltv                 15

# One-hot encoding of categorical features
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
df_4 = pd.merge(origination, df_3['is_deliquent'], left_index=True, right_index=True)\
    .set_index('is_deliquent', append=True)

# look at roc auc for numeric/continuous features
__ = df_4[numeric_features].dropna()
tgt = __.index.get_level_values(1)
__ = __.apply(lambda clmn: roc_auc_score(tgt, clmn)).sort_values(ascending=False)
print(__)
# Cltv slightly lower than ltv
numeric_features.remove('cltv')

# look at mutual information of discrete features and target
target = df_4.index.get_level_values(1).values
discrete_features = df_4.loc[:, "is_first_time_home_buyer_Y":]
_ = pd.DataFrame(index=discrete_features.columns, columns=['mutual_info'])
_['mutual_info'] = mutual_info_classif(discrete_features, target, discrete_features=True)
_['mutual_info_pct'] = _['mutual_info']/_.mutual_info.max()
_['variance'] = discrete_features.var()
_['variance_pct'] = _.variance/_.variance.max()
_['kount'] = df_4[_.index].sum()

sns.distplot(_.variance)
plt.grid()

# Look at features with maximum mutual information
# problem w/ msa_38060.0

_.sort_values('mutual_info', inplace=True, ascending=False)
print(_.head(20))

# Keep features w/variance_pct >= 2% & mutual_info >= x%
cols_to_use = list(_[(_.variance_pct >= 0.02) & (_.mutual_info_pct >= 0)].index.values) + numeric_features
df_5 = df_4[cols_to_use]

print(df_5.index.get_level_values(1).value_counts(normalize=True) * 100)
# Very imbalanced dataset (0.73% deliquent)

# Modeling - start with small sample of data
df_6 = df_5.dropna().sample(frac=0.5)

# compute scale factor
vals = df_6.index.get_level_values(1).value_counts().values
scale_pos_weight = vals[0]/vals[1]
print(f"scale factor = {scale_pos_weight:.2f}")

X, y = df_6.iloc[:, :-1], df_6.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)


########################################################################################################################
# Train xgboost
alg = XGBClassifier(objective='binary:logistic',
                    scale_pos_weight=scale_pos_weight)

st_2 = datetime.now()
alg.fit(X_train, y_train, eval_metric='auc')
print(f"time to train xgboost model: {datetime.now() - st_2}")

# Is our model predicting just one class?
predictions = alg.predict(X_test)
print(np.unique(predictions))
pred_proba = alg.predict_proba(X_test)[:, 1]

print(f"accuracy score : {accuracy_score(y_test, predictions):.2f}")
print(f"roc auc score: {roc_auc_score(y_test, pred_proba):.2f}")
print(f"f1 score: {f1_score(y_test, predictions):.2f}")

fpr, tpr, nope = metrics.roc_curve(y_test,  pred_proba)
auc = roc_auc_score(y_test, pred_proba)
plt.plot(fpr, tpr, label=f"auc = {auc:.2f}")
plt.grid()
plt.legend(loc=4)
plt.show()

feat_imp = alg.feature_importances_
feat = X_train.columns.tolist()
res_df = pd.DataFrame({'features': feat, 'importance': feat_imp}).sort_values(by='importance', ascending=False)
# res_df.plot('Features', 'Importance', kind='bar', title='Feature Importances')
# plt.ylabel('Feature Importance Score')
# plt.show()
print(res_df.head(20))
print(res_df["features"].tolist())
