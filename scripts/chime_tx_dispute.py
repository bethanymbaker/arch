import pandas as pd

filepath = '/Users/bethanybaker/Desktop/maverik_chime'

with open(filepath, mode='r') as f:
    res = f.readlines()

res = [_.strip() for _ in res if len(_) > 1]

res = res[1:len(res) - 2]

lst = []
total = 0
for idx in list(range(0, 92, 4)):
    name = res[idx]
    typee = res[idx + 1]
    date = res[idx + 2]
    amount = float(res[idx + 3].replace('- $', ''))
    total += amount
    lst.append((amount, date, f'{name}-{typee}'))

lst
print(total)

df = pd.DataFrame(lst, columns=['amount', 'date', 'description'])
df['kount'] = range(1, len(df) + 1)
df = df[['kount', 'amount', 'date', 'description']]
df.to_clipboard(index=False)

