import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
# sns.set()

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

origination_data_file = "~/Desktop/historical_data1_2009/historical_data1_Q12009/historical_data1_Q12009.txt"
monthly_performance_data_file = \
    "~/Desktop/historical_data1_2009/historical_data1_Q12009/historical_data1_time_Q12009.txt"

origination_names = ["fico", "dt_first_pi", "flag_fthb", "dt_matr", "cd_msa", "mi_pct", "cnt_units", "occpy_sts",
                     "cltv", "dti", "orig_upb", "ltv", "int_rt", "channel", "ppmt_pnlty", "prod_type", "st",
                     "prop_type", "zipcode", "id_loan", "loan_purpose", "orig_loan_term", "cnt_borr", "seller_name",
                     "servicer_name", "flag_sc"]
performance_names = ["id_loan", "svcg_cycle", "current_upb", "delq_sts", "loan_age", "mths_remng", "repch_flag",
                     "flag_mod", "cd_zero_bal", "dt_zero_bal", "current_int_rt", "non_int_brng_upb", "dt_lst_pi",
                     "mi_recoveries", "net_sale_proceeds", "non_mi_recoveries", "expenses", "legal_costs",
                     "maint_pres_costs", "taxes_ins_costs", "misc_costs", "actual_loss", "modcost", "stepmod_ind",
                     "dpm_ind", "eltv"]

origination = pd.read_csv(origination_data_file, header=None, delimiter='|', names=origination_names,
                          na_values={'fico': 9999, 'flag_fthb': 9, 'mi_pct': 999, 'cnt_units': 99, 'occpy_sts': 9},
                          dtype={'mi_pct': str, 'occpy_sts': 'category'})
origination.dt_first_pi = pd.to_datetime(origination['dt_first_pi'], format="%Y%m")
origination.dt_matr = pd.to_datetime(origination['dt_matr'], format="%Y%m")
origination.flag_fthb = origination.flag_fthb.map({'Y': True, 'N': False}).astype(bool)
origination.cd_msa = origination.cd_msa.astype('category').cat.codes

# Look at distribution of fico scored
# sns.distplot(origination.fico[~origination.fico.isna()])
# plt.title('Distribution of credit scores')
# plt.grid()

st = datetime.now()
performance = pd.read_csv(monthly_performance_data_file, header=None, delimiter="|", names=performance_names)
print(f"time to read csvs: {datetime.now() - st}")


