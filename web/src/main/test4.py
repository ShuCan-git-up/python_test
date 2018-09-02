#coding=utf-8


# for可以遍历任何序列的项目如一个列表或者一个字符串
# for lette in "letter":
#     print lette,


# fruit = {"apple", 'orange', 'watermelon'}
# for fruit_i in fruit:
#     print fruit
# #这是输出
# #set(['orange', 'watermelon', 'apple'])
# #set(['orange', 'watermelon', 'apple'])
# #set(['orange', 'watermelon', 'apple'])

# fruit = ["apple", 'orange', 'watermelon']
# for index in range(len(fruit)):
#     print fruit[index]
#
# print fruit.__len__()
#
# print range(len(fruit))
#
# print range(10,20)

# 素数
# i=2
# while(i < 100):
#    j=2
#    while(j<=(i/j)):
#        if not(i%j):break
#        j = j + 1
#    if (j > i/j) : print i, " 是素数"
#    i = i + 1


# import math
# print dir(math)
# print math.pi
# print math.e
#
# print "\a"


# print "my name is %s and age is %d" % ("舒灿", 23)

list1 = ["1", "2", 3]
list2 = ["1", "2", "3"]
#Python 3.X 的版本中已经没有 cmp 函数，如果你需要实现比较功能，需要引入 operator 模块，适合任何对象
print cmp(list1, list2)

# 默认Pop出最后一个index=-1，可以自己设定
print list1.pop();
print list1

tup = (1)
print tup

#任意无符号的对象，以逗号隔开，默认为元组