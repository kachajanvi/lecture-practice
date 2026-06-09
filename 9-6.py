#raise keyword
#raise exception type("error message")
age=-5
if age<0:
    raise ValueError("age cannot be negative")

#assert key word in python
#assert condition,"error message"
num = 10
assert num>0,"number must be positive"

print("valid number")

#custom exception with try-exept
class InsufficientBalanceError(Exception):
  pass

balance = 1000
withdraw = 1500

try:
    if withdraw>balance:
        raise InsufficientBalanceError("not enough balance")

    print("Error:",e)

except InsufficientBalanceError as e:
    print("error:",e)

#check even number using type error and value error
def check_even():
    num=int(input("enter an integer:"))

    if not isinstance(num,int):
        raise typeerror("input must be an integer")
    if num % 2!=0:
        raise ValueError("number is odd")
    print("number is even.")

try:
    check_even()
except ValueError:
    print("enter value must be only numbers.")
except exception as e:
    print("error:",e)'
#student grade validation
class InvalidGradeError(Exception):
    pass

try:
    grade=int(input("enter grade:"))
    assert grade !="","grade input cannot be empty"

    if grade <0 or grade> 100:
        raise ValueError("grade must be between ot 100")
    if grade <40:
        raise InvalidGradeError("student has failed.")
    print("student passed.")

except AssertionError as e:
    print("AssertionError :",e)
except ValueError as e:
    print("ValueError :",e)
except InvalidGradeError as e:
    print("InvalidGradeError :",e)

#temperature conversion validation
class hightemperatureerror(Exception):
    pass

try:
    temp=float(input("enter temperature in celsius:"))

    if not isinstance(temp,(int,float)):
        raise TypeError("temperature must be a number")
    assert-273<=temp<=10000,("temperature out of valid range.")

    if temp>1000:
        raise highTemperatureError("temperature exceed 1000 C")

    print("valid temperature:",temp,"C")

except TypeError as e:
    print("TypeError:",e)
except AssertionError as e:
    print("AssertionError:",e)
except HighTemperatureError as e:
    print("HighTemperatureError:",e)
    
