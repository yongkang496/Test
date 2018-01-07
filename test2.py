#coding=utf-8
__author__ = 'yongkang'
Date = '2018/1/6'

# def power(x,n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
# print(power(5,2))
# print(power(5,3))

# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# print(calc([1,2,3]))

'''
可变参数
'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3))

'''
关键字参数
'''

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

exter = {'city':'beijing','job':'engineer'}
person('paul',30,city = exter['city'],job = exter['job'])
person('paul',30,**exter)

'''
命名关键字参数
'''

def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
person('jordan',30,city = 'beijing',job = 'farmer')