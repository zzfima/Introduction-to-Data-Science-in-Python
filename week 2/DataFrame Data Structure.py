import pandas as pd

record1 = pd.Series({
    'Name': 'Alex',
    'Class': 'Physics',
    'Grade': 85
})

record2 = pd.Series({
    'Name': 'Jack',
    'Class': 'Chemistry',
    'Grade': 82
})

record3 = pd.Series({
    'Name': 'Helen',
    'Class': 'Biology',
    'Grade': 90
})

print(record1)
print(record2)
print(record3)

print('DataFrame 1')
df = pd.DataFrame()
df.insert(0, 'school1', record1)
df.insert(1, 'school2', record2)
df.insert(2, 'school3', record3)
print(df)

print('DataFrame 2')
df1 = pd.DataFrame([record1, record2, record3], index=['school1', 'school2', 'school1'])
print(df1)
print(df1.T)
school1_names = df1.loc['school1']['Name']
print(school1_names)
print(school1_names.T)

print(type(df1.loc['school2']))
print(df1.loc[:, ['Name', 'Grade']])
