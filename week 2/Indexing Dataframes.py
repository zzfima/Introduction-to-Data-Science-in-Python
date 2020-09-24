import pandas as pd

df = pd.read_csv('../week 1/mpg.csv', index_col=0)
print(df.head())
df["SN"] = df.index
print(df.head())
df = df.set_index('year')
print(df.head())
