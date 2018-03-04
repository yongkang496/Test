#coding=utf-8
__author__ = 'yongkang'
Date = '2018/3/4'
'''
类和实例
'''
class Student():
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s:%s" %(self.name,self.score))

    def get_grade(self):
        if self.score > 80:
            print('A')
        elif 60 <= self.score <= 80:
            print('B')
        else:
            print('C')


bert = Student("BOB",59)
hert = Student("David",81)
# Student.print_score(bert)
# bert.print_score()
bert.get_grade()
hert.get_grade()