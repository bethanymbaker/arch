#
# /**
# Interview Problem Statement
#
# This challenge is meant to assess the candidates ability to perform operations in the spark framework. You may either use RDDs or DataFrames to complete the challenge.
#
# 1. Start by creating a RDD/DF representing the data below
# 2. Within each group of column A and for each of the distinct terms in column B, calculate the ratio of the "current term" count vs. the "current term" count plus the "most frequent term which is not the current" count.
# 3. End with a RDD/DF that includes the column A, the distinct terms in column B, and the ratio mentioned earlier as column C.
#
#
#                 Input:
#                 +---+-----+
#                 |  a|    b|
#                 +---+-----+
#                 |  1|  cat|
#                 |  1|  cat|
#                 |  1|  dog|
#                 |  1|mouse|
#                 |  2|mouse|
#                 |  3|  cat|
#                 |  3|  dog|
#                 |  3|  dog|
#                 |  3|  dog|
#                 |  3|  dog|
#                 +---+-----+
#                 Output:
#                 +---+-----+------------------+
#                 |  a|    b|             ratio|
#                 +---+-----+------------------+
#                 |  1|  cat|0.6666666666666666|  (2 / (2 + 1))
#                 |  1|  dog|0.3333333333333333|  (1 / (1 + 2))
#                 |  1|mouse|0.3333333333333333|  (1 / (1 + 2))
#                 |  2|mouse|               1.0|  (1 / (1 + 0))
#                 |  3|  cat|               0.2|
#                 |  3|  dog|               0.8|
#                 +---+-----+------------------+


import pandas as pd

a = [1, 1, 1, 1, 2, 3, 3, 3, 3, 3]
b = ['cat', 'cat', 'dog', 'mouse', 'mouse', 'cat', 'dog', 'dog', 'dog', 'dog']

df = pd.DataFrame(data={'a': a, 'b': b})
df_1 = df.groupby(['a', 'b']).size().reset_index()
df_1.columns = ['a', 'b', 'kount']

vals = []

for idx, ser in df_1.iterrows():
    a = ser.a
    b = ser.b
    df_2 = df_1[(df_1.a == a) & (df_1.b != b)]
    val = df_2.kount.max()
    vals.append(val)

df_1['other'] = vals
df_1.fillna(0, inplace=True)
df_1['other_kount'] = df_1['other'] + df_1['kount']

df_1['ratio'] = df_1['kount'].div(df_1['other_kount'])

print(df_1[['a', 'b', 'ratio']])
