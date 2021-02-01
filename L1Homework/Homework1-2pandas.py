# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:15:32 2021

@author: ZhangFangchen
"""


import pandas as pd
from pandas import Series, DataFrame
data = {'Name':['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'],'Chinese': [68, 95, 98, 90, 80], 'Math': [65, 76, 86, 88, 90], 'English': [30, 98, 88, 77, 90]}
df1 = DataFrame(data, index=[0,1,2,3,4], columns=['Name', 'Chinese', 'Math', 'English'])
print(df1)

print("平均分为：\n",df1.mean())

print("最低分为：\n",df1.min())

print("最高分为：\n",df1.max())

print("方差为：\n",df1.std())

print("标准差为：\n",df1.var())

'''a = sum(df1.loc['ZhangFei'])
b = sum(df1.loc['GuanYu'])
c = sum(df1.loc['LiuBei'])
d = sum(df1.loc['DianWei'])
e = sum(df1.loc['XuChu'])

data = {'Sum':[a, b, c, d, e]}
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns=['Sum'])

df2.sort_values('Sum',ascending=False)
print (df2)'''

print(df1.iloc[0:].sum(axis = 1))
df1['Sum']=df1.iloc[0:].sum(axis = 1)

df2 = df1.sort_values('Sum', ascending=False)

print(df2)
