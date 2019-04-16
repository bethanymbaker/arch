import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

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

origination = pd.read_csv(origination_data_file, header=None, delimiter='|')
performance = pd.read_csv(monthly_performance_data_file, header=None, delimiter="|")
