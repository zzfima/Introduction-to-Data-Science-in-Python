import pandas as pd

df = pd.read_csv('week 2/class-grades.csv', error_bad_lines=False)
print(df.head())
