import re

import pandas as pd


def split_name(row):
    row['First'] = row['president'].split(' ')[0]
    row['Last'] = row['president'].split(' ')[-1]
    return row


df = pd.read_csv('us_presidents.csv', index_col=0)
print(df.head())
print(df.apply(split_name, axis='columns').head())
pattern = "(P<Fist>^[\w]*)(?:.*)(P<Last>[\w]*$)"
print(df['president'].str.extract(pattern).head())

for i in re.finditer(r"(^[\w]*)(?:.*)([\w]*$)", df['president']):
    print(i)
