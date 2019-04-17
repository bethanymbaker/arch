import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# sns.set()

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
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
    dumm = pd.get_dummies(new_col, prefix=col, drop_first=True, dummy_na=True)
    for coll in dumm.columns:
        origination[coll] = dumm[coll]
    del origination[col]

origination.set_index(['id_loan', 'first_payment_date', 'maturity_date'], inplace=True)
del origination['seller_name']
del origination['servicer_name']

# Look at distributions
# sns.distplot(origination.fico[~origination.fico.isna()])
# plt.title('Distribution of credit scores')
# plt.grid()

# sns.distplot(origination.mort_ins_pct[~origination.mort_ins_pct.isna() & (origination.mort_ins_pct != 0)])
# plt.title('Distribution of mortgage insurance percentage (%)')
# plt.grid()


# Performance wrangling
monthly_performance_data_file = \
    "~/Desktop/historical_data1_2009/historical_data1_Q12009/historical_data1_time_Q12009.txt"
performance_names = ["id_loan", "monthly_reporting_period", "current_upb", "delq_sts", "loan_age", "mths_remng",
                     "repch_flag", "flag_mod", "cd_zero_bal", "dt_zero_bal", "current_int_rt", "non_int_brng_upb",
                     "dt_lst_pi", "mi_recoveries", "net_sale_proceeds", "non_mi_recoveries", "expenses", "legal_costs",
                     "maint_pres_costs", "taxes_ins_costs", "misc_costs", "actual_loss", "modcost", "stepmod_ind",
                     "dpm_ind", "eltv"]
st = datetime.now()
performance = pd.read_csv(monthly_performance_data_file, header=None, delimiter="|", names=performance_names,
                          na_values={'delq_sts': 'XX'},
                          dtype={'delq_sts': 'category'})
print(f"time to read csvs: {datetime.now() - st}")
performance.monthly_reporting_period = pd.to_datetime(performance.monthly_reporting_period, format='%Y%m')

tmp = performance[['id_loan', 'loan_age', 'delq_sts']].copy()

test = pd.pivot_table(index=performance.id_loan,
                      columns=performance.loan_age,
                      values=performance.delq_sts,
                      data=performance)

