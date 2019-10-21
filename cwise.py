import pandas as pd


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 200)

user = pd.read_csv('~/Desktop/user.csv')
survey = pd.read_csv('~/Desktop/user_survey.csv')
invite = pd.read_csv('~/Desktop/user_invite.csv')


d = invite.groupby('user_id')['invitee_email_address'].nunique()

d.value_counts().sort_index().head(50).plot(kind='bar', grid=True)

import seaborn as sns
import matplotlib.pyplot as plt

sns.distplot(d.value_counts())
plt.grid()


roles = survey[survey.question_type == 'WhatIsYourCurrentPosition'].copy()[['user_id', 'response_type']]
roles.columns = ['user_id', 'position']

user = pd.merge(user, roles, on='user_id', how='left')

invite = pd.merge(invite, roles, on='user_id', how='left')

df = invite.groupby('position')['invitee_email_address'].nunique()

df.sort_values(ascending=False).plot(kind='bar', grid='True')
plt.xticks(rotation=45, ha='right')
plt.gcf().tight_layout()