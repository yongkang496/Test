#coding=utf-8
__author__ = 'yongkang'
Date = '2018/1/28'
'''
列表生成式
'''
print(list(range(1,11)))

L = []

for x in range(1,11):
    L.append(x * x)

print(L)

print([x * x for x in range(1,11)])

#偶数的平方
print([x * x for x in range(1,11) if x%2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])