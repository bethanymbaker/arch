import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from dask.distributed import Client

client = Client(n_workers=4, threads_per_worker=1)
print(client)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)
pd.set_option('display.max_colwidth', 100)

df = pd.read_csv('~/Desktop/maven_wave/Baker - Lending Club Data - DR_Demo_Lending_Club.csv',
                 index_col='Id',
                 parse_dates=['earliest_cr_line'],
                 dtype={'is_bad': bool})

# Remove invalid dates
df.loc[df.earliest_cr_line >= pd.to_datetime('2020-01-01'), 'earliest_cr_line'] = pd.NaT
df['earliest_cr_cohort'] = df.earliest_cr_line.dt.strftime('%Y')
df['pymnt_plan'] = df.pymnt_plan.map({'y': True, 'n': False})
df.groupby('earliest_cr_cohort').size().plot(grid=True, label='num_loans')
plt.legend()
plt.title('Year of Earliest Credit Line')

df.isna().sum().sort_values(ascending=False)

df.select_dtypes(include='object').nunique().sort_values(ascending=False).plot(kind='bar', grid=True)
plt.xticks(rotation=45, ha='right')
plt.title('Number of Unique Values Per Feature')
plt.xticks(rotation=45, ha='right')
plt.gcf().tight_layout()

plt.figure(figsize=(8, 6))
corr = df.select_dtypes(include=[np.number, bool]).drop(columns=['collections_12_mths_ex_med']).corr()
sns.heatmap(corr, annot=False, cmap=plt.cm.Reds)
plt.xticks(rotation=45, ha='right')
plt.gcf().tight_layout()

corr_2 = corr.unstack().to_frame('value').reset_index()
corr_2 = corr_2[corr_2.level_0 != corr_2.level_1]

tmp = corr_2[corr_2.level_0 == 'is_bad'].rename(columns={'level_1': 'feature'}).set_index('feature')[
    ['value']].sort_values('value', ascending=False)
tmp.plot(kind='bar', grid=True, legend=None)
plt.title('Correlation to is_bad')
plt.xticks(rotation='45', ha='right')
plt.gcf().tight_layout()

corr_2['features_set'] = corr_2.apply(lambda row: str(sorted([row.level_0, row.level_1])), axis=1)
corr_2 = corr_2.drop_duplicates(subset=['features_set']) \
    .drop(columns=['level_0', 'level_1']) \
    .sort_values('value', ascending=False).dropna()
sns.distplot(corr_2.value)
plt.title('Correlation Values Between Numeric Features')
plt.grid()

scaler = preprocessing.MinMaxScaler()
df_scale = pd.DataFrame(index=df.select_dtypes(include=[np.number, bool]).index,
                        data=scaler.fit_transform(df.select_dtypes(include=[np.number, bool])),
                        columns=df.select_dtypes(include=[np.number, bool]).columns)
sns.distplot(df_scale.var())
plt.title('Variance of normalized numeric features')
plt.grid()
