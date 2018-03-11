#coding=utf-8
__author__ = 'yongkang'
Date = '2018/3/11'
'''
继承和多态
'''

class Animal():
    def run(self):
        print("Animal is running...")

class Cat(Animal):
    def eat(self):
        print("Cat is eating...")
    def run(self):
        print("Cat is running...")

class Dog(Animal):
    def eat(self):
        print("Dog is eating...")
    def run(self):
        print("Dog is running...")

cat = Cat()
cat.run()
cat.eat()
dog = Dog()
dog.run()
dog.eat()


