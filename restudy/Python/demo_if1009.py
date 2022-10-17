# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   python51
# FileName:      demo_if1009.py
# Author:        xm
# Datetime:      2022/10/9 15:54
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 变量用名词，方法用动词
# ---------------------------------------------------------------------------


# 1、如果if后面的布尔表达式值为True或者一个具体的某个值就执行if下的代码块，如果为False就不执行
if 6>3:
    print(11111)
if True:
    print(2222)

# if.....else...

# 2、如果if后面的布尔表达式值为True就执行if下的代码块，如果为False就执行else下的代码块。
# num1 = int(input('请输入一个整数：'))# input函数表示从控制台(键盘)输入的任何内容都是字符串
#
# if num1>3:
#     print(111)
# else:# else和最近的那个if进行配对，它不能单独存在，需要和if搭配.但是if可以单独存在
#     print(2222)


# 字符串和int类型之间的转换
str1 = '124'
num = int(str1)# 将字符串类型的数字转换为int，使用int函数
print(num,type(num))
num1 = 890
str2 = str(num1)
print(str2,type(str2))

# 3、if...elif...elif...else...表示多条件判断，如果满足第一个条件就执行第一个操作，如果满足第二个条件就执行第二个操作，...，如果都不满足就执行else后面的操作。


if 8:
    print(88888)
if 9:
    print(99999)
if 10:
    print(10101010)

if 8:
    print(8888)
elif 9:
    print(99999)
elif 10:
    print(1010110)

num = int(input("请输入一个整数："))
if num<60:
    print('奖励一个巴巴掌')
elif num>=60 and num<80:
    print('成绩良好，奖励一朵小红花')
elif num >=80 and num<100:
    print('成绩优秀，奖励刘金重')
elif num==100:
    print('成绩100分，奖励一只陈桂林')
else:
    print('输入的数据不符合条件，请重新run')


# 要求从键盘输入一个整数，如果该整数是偶数，就打印出该整数，否则打印"不是偶数"
num11 = int(input('请输入一个整数：'))
if num11%2==0:
    print(num11)
else:
    print('不是偶数')


