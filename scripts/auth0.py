import pandas as pd
import json

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', 150)

# df = pd.read_csv('~/Downloads/all-the-news-2-1.csv')
df = pd.read_csv('~/Desktop/root/job_descriptions/crunchbase/data/pageviews.csv')
print(df.shape)
print(df.head())

# df.article_title.drop_duplicates().to_csv('~/Desktop/2020-09-11_Article-Titles.csv', index=False, header=False)
titlez = pd.read_csv('~/Desktop/2020-09-11_Article-Titles.csv', header=None)

res_file_path = '/Users/bethanybaker/Desktop/2020-09-11_NER-Output.json'

with open(res_file_path, 'r') as f:
    linez = f.readlines()

res = []
for line in linez:
    res.append(json.loads(line))

entities = []
for d in res:
    if len(d['Entities']) > 0:
        for entity in d['Entities']:
            score = entity['Score']
            text = entity['Text']
            typee = entity['Type']
            entities.append({'score': score, 'text': text, 'type': typee})

s = pd.DataFrame(entities)
