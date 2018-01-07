#coding=utf-8
__author__ = 'yongkang'
Date = '2018/1/7'
'''
递归函数
'''

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(3))
