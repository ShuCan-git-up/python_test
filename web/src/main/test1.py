#coding=utf-8
# 默认编码是ASCII 文件需要存储成utf-8才能编译通过

import sys
def  hello(name):
    strHello='Hello, '+name
    return strHello;

print (hello("Python!"))
print (hello("舒灿，开始努力学习python吧"))


def if_else(boolean):
    if boolean:
        print hello("对的")
    else:
     print hello("错的")

print if_else(True)

shucan1 = 1
shucan2 = 2
shucan3 = 3
total = shucan1 + \
        shucan2 + \
        shucan3
'''
print total
'''

day = ["monday", "tuesday", "wednesday", "thursday", "friday"]
print day[0]

#string1 = "monday"
string2 = 'tuesday'
string3 = '''wednesday'''

# for_input = raw_input("请输入，回车键退出")
# print for_input


x = 1
y = 2

# python输出默认是换行的
print x,
print y

print sys.argv