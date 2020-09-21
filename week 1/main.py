import csv
import datetime as dt
import time

with open(r"week 1\mpg.csv") as csvFile:
    dr = csv.DictReader(csvFile)
    mpg = list(dr)

print(mpg[0].keys())

print(f'City average MPG:     {sum(int(i["cty"]) for i in mpg) / len(mpg)}')
print(f'High way average MPG: {sum(int(h["hwy"]) for h in mpg) / len(mpg)}')

# city MPG  grouped by the number of cylinders a car has
# get cylinders types into dictionary
cylinders = set((int(c['cyl']) for c in mpg))

# crete dictionary of cylinders types
cylinders_dict = dict()
for c in cylinders:
    cylinders_dict[c] = []

# append to dictionary cyl-cty
for m in mpg:
    cylinders_dict[int(m['cyl'])].append(m['cty'])

print(cylinders_dict)

ctyMpgByCylinder = []
for c in cylinders:
    sum_mpg = 0
    cnt_cty = 0
    for m in mpg:
        if int(m['cyl']) == c:
            sum_mpg += int(m['cty'])
            cnt_cty += 1
    ctyMpgByCylinder.append((c, sum_mpg / cnt_cty))

print(ctyMpgByCylinder)
ctyMpgByCylinder.sort(key=lambda x: x[0])
print(ctyMpgByCylinder)

# high way  MPG  grouped by the number of vehicle classes
classes = set(c['class'] for c in mpg)

classes_dict = dict()
for c in classes:
    classes_dict[c] = []

for m in mpg:
    classes_dict[m['class']].append(m['hwy'])

avg_cls_hwy = []
for k in classes_dict:
    avg_cls_hwy.append((k, sum(int(c) for c in classes_dict[k]) / len(classes_dict[k])))

print(avg_cls_hwy)

dtnow = dt.datetime.fromtimestamp(time.time())
print(dtnow)
print(dtnow.year)

quarantine_at_home = 14
day_i_was_in_unhappy_bus = dt.datetime.fromtimestamp(time.time())
delta = dt.timedelta(days=quarantine_at_home)
print(f'I will back to work at {(day_i_was_in_unhappy_bus + delta).strftime("%d-%m-%Y")}')

store1 = [10, 11, 12, 2]
store2 = [9, 11, 12, 1]

cheapest = map(min, store1, store2)
print(list(cheapest))

myfunc = lambda a, b, c: a + b + c
print(myfunc(1, 1, 2))


def times_tables():
    lst = []
    for i in range(10):
        for j in range(10):
            lst.append(i * j)
    return lst


print(times_tables())

print([j * i for i in range(10) for j in range(10)])

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [a + b + c + d
          for a in lowercase
          for b in lowercase
          for c in digits
          for d in digits][0:10]
print(answer)
