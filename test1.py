#coding=utf-8
__author__ = 'yongkang'
Date = '2018/1/4'

# def my_abs(x):
#     if x >= 0:
#         print(x)
#     else:
#         print(-x)
#
# my_abs(-99)

# def my_abs(x):
#     if not isinstance(x,(float,int)):
#         raise TypeError("类型错误")
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# print(my_abs(-99))

import math

def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx,ny

print(move(100,100,60,math.pi/6))