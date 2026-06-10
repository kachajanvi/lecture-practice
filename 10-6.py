#polymorphism
#(1)method overloading
class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c

obj = calculator()
print(obj.add(10,20))
print(obj.add(10,20,30))

#(2)method overloading
class Animal:
    def sound(self):
        print("Animal make sound")

class dog(Animal):
    def sound(self):
        print("dog sound")

obj = dog()
obj.sound()

#issubclass()
#issubclass(child_class,parent_class)
class animal():
    pass
class dog(animal):
    pass
print(issubclass(dog,animal))
print(issubclass(animal,dog))

#super()keyword
class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks = marks
    def display(self):
        print("name:",self.name)
        print("marks:",self.marks)
obj = student("janvi",85)
obj.display()

#using super() with constructor
class parent:
    def __init__(self):
        print("parent constructor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("child constructor")
obj = child()

#access parent class method
class animal:
    def sound(self):
        print("animal make sound")
class dog(animal):
    def sound(self):
        super().sound()
        print("dog sound.")
obj = dog()
obj.sound()

#parent class and child class both have variable
class person:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
class student(person):
    def __init__(self,name,marks):
        super().__init__(name,marks)
    def display(self):
        print("name:",self.name)
        print("marks:",self.marks)

obj = student("janvi",85)
obj.display()
