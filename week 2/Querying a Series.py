import numpy as np
import pandas as pd

pd_arr = pd.Series(np.random.randint(0, 1000, 10000))
print(pd_arr)
print(pd_arr.head())
total = 0
for i in pd_arr:
    total += i
print(total)
print(np.sum(pd_arr))

pd_arr += 2
print(pd_arr.head())

# for k, v in pd_arr.iteritems():
#     pd_arr._set_value(k, v + 2)
#
# for k, v in pd_arr.iteritems():
#     pd_arr.loc[k] = v + 2

print(pd_arr.dtype)
pd_arr.loc[10000] = 1
print(pd_arr.dtype)
pd_arr.loc[10001] = 'k'
print(pd_arr.dtype)

print('s')
s = pd.Series([1, 2, 3])
print(s)

s.loc['fuel'] = 95
print(s)

s.loc['name'] = 'no Pl1'
s.loc['name'] = 'no Pl2'

print(s)

students_classes = pd.Series({
    'Alice': 'Physics',
    'Jack': 'Chemistry',
    'Molly': 'English',
    'Sam': 'History'
})
print(students_classes)

kelly_classes = pd.Series(['Philosophy', 'Arts', 'Math'], index=['Kelly', 'Kelly', 'Kelly'])
print(kelly_classes)
print(kelly_classes.loc['Kelly'])

all_student_classes = students_classes.append(kelly_classes)
print(all_student_classes)
print(all_student_classes.loc['Kelly'])
