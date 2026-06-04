#oop
#class and object
#student class
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("name:",self.name)
        print("age:",self.age)

s1=student("vivek",26)
s2=student("rahul",20)

s1.display()
s2.display()

#self keyword
#employee
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show(self):
        print("employee name:",self.name)
        print("salary:",self.salary)

e1=employee("rahul",50000)
e1.show()

#del keyword
#delete variables
x=100
print(x)
del x

#student
class student:
    def __init__(self):
        self.name="janvi"

s1=student()
del s1
del s1.name
print(s1)

#encapsulation
class bankaccount:
    def __init__(self):
        self. __balance=100000
 
    def deposite(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        self.__balance -= amount

 from abc import ABC, abstractmethod   def get_balance(self):
        return self.__balance

acc1=bankaccount()
acc1.deposite(50000)
acc1.withdraw(100000)

print("account blance:",acc1.get_balance())

#polymorphism
#method overloading
class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        print("dog bhoe bhow")
class snack(animal):
    def sound(self):
        print("snack shreeeeeeeeee....")

d=dog()
s=snack()

d.sound()
s.sound()

#same function different object
class car:
    def move(self):
        print("car is running.")
class plane:
    def move(self):
        print("plan is flying.")

    def action(vehical):
        vehicle.move()

c=car()
p=plane()

action(c)
action(p)

#abstraction
#vehicle
from abc import ABC, abstractmethod
class vehicle(ABC):
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car started.")
class bike(vehicle):
    def start(self):
        print("bike started!")

c=car()
b=bike()

c.start()
b.start()

#inheritance
#1.single inheritance
class parent:
    def show(self):
        print("parent class")
class child(parent):
    pass

c=child()
c.show

#2.multilevel inheritance
class grantparent:
    def title(self):
        print("grandparent")
class parent(grantparent):
    def title1(self):
        print("parent")
class child(parent):
    def title2(self):
        print("child")

obj=child()

obj.title()
obj.title1()
obj.title2()

#3.multiple inheritance
class father:
    def father_property(self):
        print("car")
class mother:
    def mother_property(self):
        print("jewellery")
class child(father,mother):
        pass

c=child()

c.father_property()
c.mother_property()

#4.hierachical inheritance
class parent:
    def display(self):
        print("parent class")
class child1(parent):
    pass
class child2(parent):
    pass

c1=child1()
c2=child2()

c1.display()
c2.display()

#5.hybrid inheritance
class A:
    def showA(self):
            print("A class")
class B(A):
    def showB(self):
            print("B class")
class C(A):
    def showC(self):
            print("C class")
class D(B,C):
     def showD(self):
            print("D class")

obj=D()

obj.showA()
obj.showB()
obj.showC()
obj.showD()

        
