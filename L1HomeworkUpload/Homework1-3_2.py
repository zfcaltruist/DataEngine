#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
df = pd.read_csv('car_complain.csv')
df.to_excel('./car_complain.xlsx', index=False)
#0代表没有，1代表存在
df = df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
#数据清洗，将别名合并
def f(x):
    x = x.replace('一汽-大众','一汽大众')
    return x
df['brand'] = df['brand'].apply(f)
#按brand统计,id出现的次数（即投诉总数）
result = df.groupby(['brand'])['id'].agg(['count'])

#从第7列开始有投诉代码
tags = df.columns[7:]

#按各投诉项tags统计
result2 = df.groupby(['brand'])[tags].agg(['sum'])

#将result2和result连接
result2 = pd.merge(result,result2, left_index=True, right_index=True, how='left')

#将索引列恢复正常
result2.reset_index(inplace=True)

#按投诉总数（count）从大到小排序
result2 = result2.sort_values('count',ascending=False)
print("各品牌投诉总数及投诉项result2\n",result2)



#按car_model和brand统计,id出现的次数（即投诉总数）
result3 = df.groupby(['brand','car_model'])['id'].agg(['count'])

#将索引列恢复正常
result3.reset_index(inplace=True)
print("各品牌+车型投诉总数result3:\n",result3)

#按brand统计,car_model出现的次数
result4 = result3.groupby(['brand'])['car_model'].agg(['count'])
result4.reset_index(inplace=True)
print("各品牌车型总数result4：\n",result4)

#按brand统计，count出现的次数
result5 = result3.groupby(['brand'])['count'].agg(['sum'])
result5.reset_index(inplace=True)
print("各品牌投诉总数result5:\n",result5)

#将result4和result5连接
result6 = pd.merge(result4,result5, how='outer')
print("各品牌车型+投诉总数result6:\n",result6)

#新增列Ratio：按品牌计，车型平均投诉数
result6['Ratio']=(result6['sum']/result6['count'])
print("各品牌车型+投诉总数+平均投诉数result6:\n",result6)

#按Ratio排列，平均投诉投诉总数
result7 = result6.sort_values('Ratio', ascending=False)
print("按Ratio排列result7:\n",result7)

#将结果保存至result7.csv
result7.to_csv("./result7.csv")


# In[ ]:




