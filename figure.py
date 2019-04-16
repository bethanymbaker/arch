import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
# sns.set()

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

# Originatin wrangling
origination_data_file = "~/Desktop/historical_data1_2009/historical_data1_Q12009/historical_data1_Q12009.txt"

origination_names = ["fico", "first_payment_date", "first_time_home_buyer", "maturity_date", "msa", "mort_ins_pct",
                     "num_units", "occpy_sts", "cltv", "dti", "orig_upb", "ltv", "int_rt", "channel", "ppmt_pnlty",
                     "prod_type", "st", "prop_type", "zipcode", "id_loan", "loan_purpose", "orig_loan_term", "cnt_borr",
                     "seller_name", "servicer_name", "flag_sc"]

origination = pd.read_csv(origination_data_file, header=None, delimiter='|', names=origination_names,
                          na_values={'fico': 9999,
                                     'first_time_home_buyer': 9,
                                     'mort_ins_pct': 999,
                                     'num_units': 99,
                                     'occpy_sts': 9,
                                     'cltv': 999,
                                     'dti': 999,
                                     'ltv': 999,
                                     'channel': 9,
                                     'prop_type': 99},
                          dtype={'occpy_sts': 'category', 'channel': 'category', 'st': 'category',
                                 'prop_type': 'category'})

origination[['first_payment_date', 'maturity_date']] = origination[['first_payment_date ', 'maturity_date']]\
    .apply(pd.to_datetime, format='%Y%m')
origination.first_time_home_buyer = origination.first_time_home_buyer.map({'Y': True, 'N': False}).astype(bool)
origination.msa = origination.msa.astype('category').cat.codes
origination.ppmt_pnlty = origination.ppmt_pnlty.map({'Y': True, 'N': False}).astype(bool)

# Look at distributions
# sns.distplot(origination.fico[~origination.fico.isna()])
# plt.title('Distribution of credit scores')
# plt.grid()

# sns.distplot(origination.mi_pct[~origination.mort_ins_pct.isna() & (origination.mort_ins_pct != 0)])
# plt.title('Distribution of mortgage insurance percentage (%)')
# plt.grid()


# Performance wrangling
monthly_performance_data_file = \
    "~/Desktop/historical_data1_2009/historical_data1_Q12009/historical_data1_time_Q12009.txt"
performance_names = ["id_loan", "svcg_cycle", "current_upb", "delq_sts", "loan_age", "mths_remng", "repch_flag",
                     "flag_mod", "cd_zero_bal", "dt_zero_bal", "current_int_rt", "non_int_brng_upb", "dt_lst_pi",
                     "mi_recoveries", "net_sale_proceeds", "non_mi_recoveries", "expenses", "legal_costs",
                     "maint_pres_costs", "taxes_ins_costs", "misc_costs", "actual_loss", "modcost", "stepmod_ind",
                     "dpm_ind", "eltv"]
# st = datetime.now()
# performance = pd.read_csv(monthly_performance_data_file, header=None, delimiter="|", names=performance_names)
# print(f"time to read csvs: {datetime.now() - st}")


