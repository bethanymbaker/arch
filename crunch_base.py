import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.parse import urlparse

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', 50)

pageviews = pd.read_csv("~/Desktop/data/pageviews.csv",
                        index_col=0,
                        parse_dates=[2]) \
    .rename(columns={'time': 'created_at'})
users = pd.read_csv("~/Desktop/data/users.csv",
                    index_col=0,
                    parse_dates=[2])

assert pageviews.user_id.nunique() == users.user_id.nunique()

users['created_at_date'] = pd.to_datetime(users.created_at.dt.strftime('%Y-%m-%d'))
pageviews['created_at_date'] = pd.to_datetime(pageviews.created_at.dt.strftime('%Y-%m-%d'))
pageviews['netloc'] = pageviews.article_url.apply(lambda url: urlparse(url).netloc)

pageviews['pageview_number'] = pageviews.groupby('user_id')['created_at'].rank('first')
pageviews['total_pageviews'] = pageviews.groupby('user_id')['pageview_number'].transform('max')
pageviews['num_visits'] = pageviews.groupby('user_id')['created_at_date'].nunique()

pageviews[pageviews.user_id == '10b2c9ab-c3fe-49cd-81a8-89761a5d372f']

# users.isna().sum()
# Out[4]:
# user_id                0
# created_at             0
# job_function       10754
# job_industry       10837
# use_case            9919
# created_at_date        0
# dtype: int64
#
# users.nunique()
# Out[8]:
# user_id            12461
# created_at         12461
# job_function          10
# job_industry          32
# use_case               8
# created_at_date      232
# dtype: int64
#
# users.job_function.value_counts(normalize=True).plot(kind='bar', grid=True)
# plt.xticks(rotation='45', ha='right')
# plt.title('Job Functions')
# plt.gcf().tight_layout()
#
# users.job_industry.value_counts(normalize=True).plot(kind='bar', grid=True)
# plt.xticks(rotation='45', ha='right')
# plt.title('Job Industry')
# plt.gcf().tight_layout()
#
# users.use_case.value_counts(normalize=True).plot(kind='bar', grid=True)
# plt.xticks(rotation='45', ha='right')
# plt.title('Use Case')
# plt.gcf().tight_layout()

# Some featurization


# Some EDA

users.groupby('created_at_date').user_id.nunique().plot(grid=True)
plt.title('User Ids Created By Date')
plt.gcf().tight_layout()

sns.distplot(pageviews.groupby('user_id').size())
plt.grid()
plt.title('Number of PageViews Per User Id')

sns.distplot(pageviews.groupby('user_id').size()[pageviews.groupby('user_id').size() <= 25])
plt.grid()
plt.title('Number of PageViews Per User Id')

pageviews.groupby('user_id').size().value_counts(normalize=True).head(10).plot(kind='bar', grid=True)

pageviews.groupby('user_id').size().to_frame('Num Pageviews').boxplot()
plt.title('Boxplot of Pageviews Per User')

pageviews.marketing_channel.value_counts()
