#Type of function

def add():
    print("welcome student!!")
add()

def multi(a,b):
    print("multiplication:",a*b)
multi(4,5)

def factorial(n):
    if(n == 1):
      return 1
    return n*factorial(n-1)

print(factorial(5))


#sum of two numbers 
def total(n):
    if n==0:
        return 0
    return n + total(n-1)

print(total(5))

#syntax
lambda argument : expression
square = lambda x:x*x

print(square(5))

add=lambda a,b:a-b
print(add(10,20))

#list
numbers=[1,2,3,4,5]
result=list(map(lambda x:x*2,numbers))

print(result)

#filter
number=[1,2,3,4,5]
odd=list(filter(lambda x:x%2!=0,numbers))

print(odd)


x=10

def show():
    print(x)

    show()

count=0

def increment():
    global count
    count =+ 1

    increment()
    increment()
    increment()

print(count)

def calculation(a,b):
    return a+b,a-b
result = calculation(10,5)

print(result)

def student():
    name="alice"
    marks=90

    return name,marks
n,m=student()

print(n)
print(m)

#built in function
number=[1,2,3,4,5]

print("length:",len(numbers))
print("maximum:",max(numbers))
print("minimum",min(numbers))

#user define function
def greet(name):
    return "hello" + name

print(greet("students"))


def add_number(*args):
    total=0

    for num in args:
        total += num
        return total

print(add_number(1,2,3,4,5))

#key word argument
def student_into(**kwargs):
    for key,value in kwargs.items():

        print(key,":",value)

student_into(name="janvi",age=20,cource="python")

#doc(documentation string)
def multiply(a,b):
    """this function returns the multiplication of two numbers"""
    return a*b

print(multiply(4,5))
print(multiply.__doc__)

#TNRN
def greet():
        print("Hello, Python Student")

greet()

#TSRN
def add(a , b):
        print("addition:",a+b)

add(10,20)

#TNRS
def message():
        return"hello students"

print(message())

#TSRS
def multiply(a,b):
    return a*b
result=multiply(4,7)

print(result)


            

        
