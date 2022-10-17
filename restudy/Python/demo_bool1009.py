# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   python51
# FileName:      demo_bool1009.py
# Author:        xm
# Datetime:      2022/10/9 14:03
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 变量用名词，方法用动词
# ---------------------------------------------------------------------------

print(True+99)
print(False+99)

print(bool(5 > 3))
print(5 > 3)
print(bool(1))
print(bool(0))# bool函数中如果是0，结果是False
print(bool(''))
print(bool([]))
print(bool({}))
print(bool(set()))

print(bool(6==8))
print(6==8)

print(bool(5<9 and 7*8==89))
print(5<9 or 7*8==89)


print(type(None))# None是NoneType类型的唯一值

if 3>2 and None:
    print(111111)
print("" == None)

# print(len(None)) #空，没有长度,所以会报错
print(len(""))#0,长度为0



a = 100
print(id(a))
a = 101
print(id(a))


list1 = [1,2,3]
print(id(list1))
list1.append(43)
print(id(list1))


# python中的常用运算符
# 1、算数运算符
print(4+3)
print(4-3)
print(4*3)
print(4/3)
print(5//2)# 取整/取商
print(5%2)# 取余/取模
print(5**3)# 幂运算


# 2、比较运算符：比较出的结果是bool值
print(5>6)
print(5>=8)
print(5<=8)
print(8==9)
print(8!=9)
# 3、逻辑运算符
print(7>9 and 9<10 or 7>=5)
print(7>9 and (9<10 or 7>=5))
print(not 7>9 and (9<10 or 7>=5))
print(not 6!=8 or 7**2==89 and 7<6 or (7>2))# 当括号、not、and和or同时存在的情况下，优先级为()>not>and>or
print(6+5>10 and 7/5==1.2 or 8**2==64)
print(8**2==64 or 6+5>10 and 7/5==1.2 )

# 4、身份运算符
a="hello world"
b="hello world"
print(a is b)# is比较的是内存地址
print(a is not b)# is比较的是内存地址
print(a==b)

str1 = '678'
str2 = str(678)
print(str2,type(str2))
print(str1 is str2)
print(str1 == str2)

# 5、成员运算符:常结合if条件判断语句使用以及循环语句中使用
print('h' not in 'hello')
if 'He' in 'hello':
    print('在里面')

for i in 'helloworld':
    print(i)

# 6、赋值运算符
a = 78
name = '小花'
kl = 6>5
print(kl)
a = 1
b = 2
c = 3
a,b,c=11,22,33# 对多个变量赋值

a=b=c=d=100# 一个值可以赋值给多个变量
# 交换变量aa和cc的值
aa=100
cc=200
aa,cc=cc,aa
print(aa)
print(cc)

# 扩展后的赋值运算符
# +=
# -=
# *=
# /=
# %=

a = 100
a+=1# 相当于a=a+1
print(a)

a=10
b=20
a+=b# 相当于a=a+b
print(a)

a-=15# a=a-15
print(a)

a*=5
print(a)

a/=3
print(a)

a**=2# a=a**2
print(a)
