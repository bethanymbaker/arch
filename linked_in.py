import pandas as pd

with open('/Users/b.baker/Desktop/linkedin_followers.txt', 'r') as f:
    dat = f.readlines()

dat_2 = [_.strip() for _ in dat if (_ != '\n' and
                                    _ != 'Following\n')]

f_dict = {}

lst = []
kount = 0
for idx in range(len(dat_2)):
    if idx % 3 == 2:
        num_followers = dat_2[idx]
        f_dict[dat_2[idx-2]] = num_followers
        lst.append({'name': dat_2[idx-2], 'num_followers': dat_2[idx]})

df = pd.DataFrame(lst[:-1])
df['num_followers'] = df.num_followers.str.replace(' followers', '')







