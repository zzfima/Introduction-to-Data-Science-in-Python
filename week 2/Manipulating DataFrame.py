import pandas as pd


def split_name(row):
    row['First'] = row['president'].split(' ')[0]
    row['Last'] = row['president'].split(' ')[-1]
    return row


df = pd.read_csv('us_presidents.csv', index_col=0)
print(df.head())
df = df.apply(split_name, axis='columns')
print(df.head())
