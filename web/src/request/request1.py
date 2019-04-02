import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')


# r = requests.get(r"https://api.github.com/users/acombs/starred")
# print(type(r.json()))  # type list
# for i, val in enumerate(r.json()):
#     print("序号: %s, 值: %s" % (i + 1, val))

# 'r'是防止字符转义的 如果路径中出现'\t'的话 不加r的话\t就会被转义 而加了'r'之后'\t'就能保留原有的样子
PATH = r'/Users/shucan/Documents/ai_study/'

r= requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

with open(PATH + 'iris.data','w') as f:
    f.write(r.text)

os.chdir(PATH)


df = pd.read_csv(PATH + 'iris.data', names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])

print(df)


print(df.ix[:3, [x for x in df.columns if 'width' in x]])

print(type(df['class'].unique()))
print('输出去重后的class: %s' % df['class'].unique())

# print(df[df['class'] =='Iris-virginica'].reset_index(drop=True))
# & 运算优先级大于 > 号
print(df[(df['class']== 'Iris-virginica') & (df['petal width'] > 2.2)])

print(df.describe())
# 查看前n行，n为参数，默认是5
print(df.head())


print(df.corr())

plt.style.use('ggplot')
fig,ax = plt.subplots(figsize=(6,4))
ax.hist(df['sepal length'], color='black')
ax.set_ylabel('数量', fontsize=12)
ax.set_xlabel('length', fontsize=12)
plt.title('莺尾花花萼的长度', fontsize=14, y=1.01)







exit()



