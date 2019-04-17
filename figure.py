import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# sns.set()

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 150)

# Originatin wrangling
origination_data_file = "~/Desktop/historical_data1_2009/historical_data1_Q12009/historical_data1_Q12009.txt"

origination_names = ["fico", "first_payment_date", "is_first_time_home_buyer", "maturity_date", "msa", "mort_ins_pct",
                     "num_units", "occpy_sts", "cltv", "dti", "orig_upb", "ltv", "interest_rate", "channel",
                     "is_ppmt_pnlty", "prod_type", "state", "prop_type", "zipcode", "id_loan", "loan_purpose",
                     "orig_loan_term", "num_borr", "seller_name", "servicer_name", "is_super_conforming"]

origination = pd.read_csv(origination_data_file,
                          header=None,
                          delimiter='|',
                          names=origination_names,
                          parse_dates=['first_payment_date', 'maturity_date'],
                          date_parser=lambda x: pd.datetime.strptime(x, '%Y%m'),
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
    .drop(columns='prod_type')

category_columns = ['is_first_time_home_buyer',
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

for col in category_columns:
    new_col = origination[col].astype('category')
    if len(new_col[new_col.isna()]) > 0:
        dumm = pd.get_dummies(new_col, prefix=col, drop_first=True, dummy_na=True)
    else:
        dumm = pd.get_dummies(new_col, prefix=col, drop_first=True)
    for coll in dumm.columns:
        origination[coll] = dumm[coll]
    del origination[col]

df = origination.copy()
df.set_index(['id_loan', 'first_payment_date'], inplace=True)
del df['maturity_date']
del df['seller_name']
del df['servicer_name']

plot_flag = False
if plot_flag:
    fig, axes = plt.subplots(3, 3, figsize=(12, 12))

    sns.distplot(df[~df['fico'].isna()]['fico'], ax=axes[0, 0])
    axes[0, 0].set_xlabel('fico')
    axes[0, 0].grid()

    sns.distplot(df[~df['mort_ins_pct'].isna() & (df.mort_ins_pct != 0)]['mort_ins_pct'], ax=axes[0, 1])
    axes[0, 1].set_xlabel('mort_ins_pct')
    axes[0, 1].grid()

    sns.distplot(df[~df['cltv'].isna()]['cltv'], ax=axes[0, 2])
    axes[0, 2].set_xlabel('cltv')
    axes[0, 2].grid()

    sns.distplot(df[~df['dti'].isna()]['dti'], ax=axes[1, 0])
    axes[1, 0].set_xlabel('dti')
    axes[1, 0].grid()

    sns.distplot(df[~df['ltv'].isna()]['ltv'], ax=axes[1, 1])
    axes[1, 1].set_xlabel('ltv')
    axes[1, 1].grid()

    sns.distplot(df[~df['interest_rate'].isna()]['interest_rate'], ax=axes[1, 2])
    axes[1, 2].set_xlabel('interest_rate')
    axes[1, 2].grid()

    sns.distplot(df[~df['num_units'].isna()]['num_units'], ax=axes[2, 0])
    axes[2, 0].set_xlabel('num_units')
    axes[2, 0].grid()

    sns.distplot(df[~df['orig_upb'].isna()]['orig_upb'], ax=axes[2, 1])
    axes[2, 1].set_xlabel('orig_upb')
    axes[2, 1].grid()

    sns.distplot(df[~df['orig_loan_term'].isna()]['orig_loan_term'], ax=axes[2, 2])
    axes[2, 2].set_xlabel('orig_loan_term')
    axes[2, 2].grid()

    fig.suptitle('Distribution of numeric features')
    fig.savefig('/Users/bethanybaker/Desktop/2019-04-17_Feature-Distributions.png')
    plt.close(fig)

# Performance wrangling
monthly_performance_data_file = \
    "~/Desktop/historical_data1_2009/historical_data1_Q12009/historical_data1_time_Q12009.txt"
performance_names = ["id_loan", "monthly_reporting_period", "current_upb", "delq_sts", "loan_age", "mths_remng",
                     "repch_flag", "flag_mod", "cd_zero_bal", "dt_zero_bal", "current_int_rt", "non_int_brng_upb",
                     "dt_lst_pi", "mi_recoveries", "net_sale_proceeds", "non_mi_recoveries", "expenses", "legal_costs",
                     "maint_pres_costs", "taxes_ins_costs", "misc_costs", "actual_loss", "modcost", "stepmod_ind",
                     "dpm_ind", "eltv"]
st = datetime.now()
performance = pd.read_csv(monthly_performance_data_file,
                          header=None,
                          delimiter="|",
                          names=performance_names,
                          usecols=['id_loan', 'monthly_reporting_period', 'delq_sts', 'cd_zero_bal'])
performance.monthly_reporting_period = pd.to_datetime(performance.monthly_reporting_period, format='%Y%m')
print(f"time to load performance data: {datetime.now() - st}")

test = pd.pivot_table(index=performance.id_loan,
                      columns=performance.loan_age,
                      values=performance.delq_sts,
                      data=performance)

