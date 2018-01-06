#coding=utf-8
__author__ = 'yongkang'
Date = '2018/1/6'

def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5,2))
print(power(5,3))