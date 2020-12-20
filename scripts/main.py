import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', 50)

df = pd.read_excel('~/Downloads/5_States_-_Large_Swings_GA.xlsx')
df['TIMESTAMP'] = pd.to_datetime(df.TIMESTAMP)