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

def my_abs(x):
    if not isinstance(x,(float,int)):
        raise TypeError("类型错误")
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))