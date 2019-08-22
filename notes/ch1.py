# _*_ coding: utf-8 _*_
# python training records

""" ch1 快速上手 基础知识
# 
#
#
"""
##基本计算功能

1 / 2      # 浮点运算，结果为0.5，python3特性
1 // 2     # 整除运算，结果为0，舍弃小数部分 向下取整；对于负数，越整到离0更远
2 ** 3     # 乘方运算符 也可使用内置函数 pow()
pow(2,3,7) # 计算2的3次方，并对7求模，结果为1
0xAF       # 16进制表示 175
0b10       # 二进制表示

##  屏幕输入输出功能
print('I am the world')
print(4*4) 
input("the number is : ") 
a= input("the number a is : ")
b= input("the number b is : ")
print(int(a)*int(b))  #类似于类型转换 其他还有 str floor
name = input("what is your name?")
print("hello," + name + "!")  # 加号可以串接字符串；双引号和单引号的意义相同

## 一些内置函数
abs(-10)    # 计算绝对值
round(2/3)  # 结果为1，圆整到最接近的整数，当距离相同时，圆整到偶数

## 模块
import math       #导入模块 
math.floor(32.9)  #模块名.函数名  floor函数为向下圆整。
math.ceil(32.9)   #向上圆整，与floor相反

from math import sqrt  ## 另一种从模块导入函数的方法 需要明确没有函数名称冲突
sqrt(9)           #平方根函数 返回3.0

from cmath import sqrt ## 专门处理复数的模块

## 字符串
print(repr("hello,\nworld"))
    >> 结果：'hello,\nworld'
print(str("hello,\nworld"))
    >> 结果：hello，
            world
# 跨越多行的字符串，可以使用三引号来实现；也可以用这个来为程序添加多行注释。
# 多行跨行，也可以用反斜杠+换行符；将被转义，即被忽略
pring (r'C:\nowhere')# 当不需要转义时，即取消反斜杠的意义；用前缀r表示原始字符串。

