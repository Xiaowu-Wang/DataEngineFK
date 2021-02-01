from pandas import Series, DataFrame
import numpy as np
import pandas as pd
# 计算
data = {'Chinese': [68, 95, 98, 90,80], 'Math': [65, 76, 86, 88, 90], 'English': [30, 98, 88, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns=['Chinese', 'Math', 'English'])
df2.rename(columns={'Chinese': '语文','Math':'数学','English': '英语'}, inplace = True)
df3=pd.DataFrame({'ZhangFei': [68,65,30], 'GuanYu': [95,76,98], 'LiuBei': [98,86,88],'DianWei':[90,88,77],'XuChu':[80,90,90]})
s=pd.DataFrame([5,2,1,4,3],index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'])
result = df3.groupby('ZhangFei').agg([np.sum]) #最大成绩求和排序不太明白
print(result)
print(df2.describe())
print(s)
