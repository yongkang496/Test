#coding=utf-8
__author__ = 'yongkang'
Date = '2018/3/4'
'''
访问限制
'''
class Student():
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s:%s" %(self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self):
        self.__score = score

bert = Student('Bob',59)
bert.score = 99
print(bert.score)
