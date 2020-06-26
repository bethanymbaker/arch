from collections import Counter

people = [
    ('1', 2000, 2010),
    ('2', 1975, 2005),
    ('3', 1975, 2003),
    ('4', 1803, 1809),
    ('5', 1750, 1869),
    ('6', 1840, 1935),
    ('7', 1803, 1921),
    ('8', 1894, 1921)
]

# person = people[0]
# years = list(range(person[1], person[2] + 1))

all_years = []
for person in people:
    years = list(range(person[1], person[2] + 1))
    all_years += years

cnt = Counter(all_years)
print(cnt.most_common())

