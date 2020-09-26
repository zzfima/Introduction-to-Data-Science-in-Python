import pandas as pd

# 1
# a = [1, 2, 3]
# b = [5, 6, 7]
# print(a + b)
# print(a.append(b))
# print(a.extend(b))
# print(a)

# 2
# np_a = np.array(a)
# np_b = np.asarray(b)
# np_a[0] = 11
# np_b[0] = 12
# a[2] = 110
# b[2] = 120
# print(a, b)

# 3
# arr = np.array([1, 2, 7, 333])
# print(np.where(arr == 7))

# 4
# mtrx = np.array([[1.3, 1.7], [2.3, 2.9]])
# print(mtrx.round(1))
# print(mtrx)
# print(round(mtrx, 1))
# print(mtrx)

# 5
# ar = np.array([2, 4, 5, 3, 7, 8, 1, 9])
# print(np.sort(ar)[-1:-4:-1])
# print(ar.sort())
# print(ar)
# #             [0  1  2  3  4  5  6  7]
# ar = np.array([2, 4, 5, 3, 7, 8, 1, 9])
# print(np.argpartition(ar, 3)[:3])
# print(ar[np.argpartition(ar, 3)[:3]])
# print(ar[np.argpartition(ar, -3)[-3:]])

# # 6
# a = np.array([[1, 1, 1],
#               [2, 2, 2],
#               [3, 3, 3]])
# b = np.array([4, 4, 4])
# print(np.append(a, b, axis=1))

# 7
# a = np.array([[1, 1, 1],
#               [2, 2, 2]])
# b = np.array([3], [3])
# print(np.append(a, b, axis=0))

# 8
# ar = np.array([1, 2, 3])
# print((ar - np.min(ar)) / np.ptp(ar))

# 9
# pd_arr = pd.DataFrame([[1,2],[3,4]])
# print(type(pd_arr.to_numpy()))

# 10
# ar = np.array([1, 2, np.NaN, 3])
# print([x for x in ar if x != np.NaN])
# np.savetxt('ddd.csv', ar, delimiter=',')

# # 12
# print(np.eye(3))
# print(np.identity(3))

# # 14
# pd_arr = pd.DataFrame([[1, 2], [3, 4]])
# pd_ser = pd.Series([1, 2, 3, 4])
# print(pd_ser[0])

# # 16
# pd_ser = pd.Series([1, 2, 3, 4])
# pd_arr = pd.DataFrame({'ggg': 555, 'hhh': 7})
# print(pd_ser)

# 17
# pd_ser = pd.Series([1, 2, 3, 4])
# pd_arr = pd.DataFrame.from_dict({'ggg': 555, 'hhh': 7})
# print(pd_ser)

# 18
pd_arr = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['a', 'b'])
print(pd_arr['b'])
print(pd_arr.loc[:, 'b'])
pd_arr['b'][0] = 77
pd_arr.loc[:, 'b'][1] = 44
print(pd_arr['b'])
print(pd_arr.loc[:, 'b'])

# 19
# pd_arr = pd.DataFrame([[1, 2], [3, 4], [5, 6], [9, 2]], columns=['a', 'b'])
# # pd_ser = pd.Series([0, 4, 2])
# pd_arr.plot(kind='area', x='a', y='b', color='red')
# plt.show()

# 20
# pd_arr = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
# # pd_arr.plot(kind='area', x='a', y='b', color='red')
# pd.plotting.scatter_matrix(pd_arr)
# plt.show()

# 24
# pd_arr = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
# sample_figure = plt.figure()
# ax1 = 1 - sample_figure.add(121) | 2 - sample_figure.add(122)
# ax1.hist(pd_arr)

# 25
# import scipy.special as sp
# print(sp.cbrt(8))

# 26
# import scipy.linalg as spla
# print(spla.inv([[1, 2], [3, 4]]))

# 28
# from scipy.optimize import minimize
# print(minimize(method=))

# 30
# import math, scipy
# from sympy import *
# def sigmoid(x):
#     return 1 / (1 + math.exp(-x))
#
# x = Symbol(x)
# y = sigmoid(x)
# Dv = y.diff

