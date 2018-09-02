#coding=utf-8

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print 'test2_opt.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test2_opt.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        print '输入的文件名为', inputfile
        print '输出的文件名为', outputfile

if __name__ == "__main__":
    main(sys.argv[1:])



"""
python有五个标准类型 numbe数字, string字符串, list列表, tuple元组(数组), dictionary字典
"""

# str = 'abc'
# print str * 3
# print '123' + str
# #不存在越界问题，直接输出到最大
# print str[1:3]

list = [123, "shucan", 2.23, [456, "xulei", 0.3]]
# print list
# print list[2:4]
# print list[-1]

#元组,元组不能二次赋值，相当于只读
tuple = ('shucan_tuple', 123, 0.23)
# print tuple
# print tuple[0:3]

# list[0] = 1234
# tuple[1] = 1234


#dictionary 是除列表list以外Python里面最灵活的内置数据结构,是无序的，通过键来存取的，而不是通过偏移 ，用{}来表示，由索引key和值value组成
dict = {}
dict['one'] = 'one_test'
dict[1] = 1

# print dict
# print dict.keys()
# print dict.values()

print int('5', 16)

print complex(1, 2)

print oct(123)
print hex(123)
print ord("s")
print unichr(97)


print 9.0 // 2

print 9/2
print 2**3

#位运算符
# 0011 0010
a = 50
# 0011 1100
b = 60

# print a&b
#
# print ~b


#逻辑运算符 and or not
x = 1
y = 2
if x and y:
    print 1
else:
    print 2

# 成员运算符
a = 1
b = 20
c = [2,3,4,5,20]
if a in c:
    print '1在列表里面'
elif b in c:
    print '20在列表里面'
else:
    print '比较完毕'


# 身份运算符 is 或者 is not 判断两个标识符是不是指向同一个对象 类似于==(具体判断的是亮哥对象的值是否相等)
# identity =  "shucan"
#
# identity1 = identity
# identity2 = identity
# if identity1 is identity2:
#     print '指向同一个对象，即同一个身份'
# else:
#     print '不指向同一个身份'

a_test = [1, 2, 3]
print a_test[:]
b_test = a_test[:]
print b_test