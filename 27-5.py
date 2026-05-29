#string formatting
name="aisha"
age=21

#using f-string
print(f"my name is {name} and i am {age} years old.")

#using.formate()
print("my name is {} and i am {} years old." .format(name , age))

#using % formatting
print("my name is % s and i am % d years old." %(name , age))

price = 199.456
print(f"price:{price:.2f}")


#list and tuple(mutability)
#list
my_list=[10,20,30]
print("original list:",my_list)

my_list[1]=200
print("modified list:",my_list)

#append
my_list.append(50)
my_list.append(60)

print("after append list:",my_list)

#remove
my_list.remove(10)
print("after remove list:",my_list)


#tuple-immutable
my_tuple=(10,20,30,40)
print("tuple:",my_tuple)

#access element
print("first tuple element:",my_tuple[1])

#indexing and slicing
text="python"

print("first letter:",text[0])
print("last letter:",text[len(text)-1])
print("last letter:",text[-1])

#slicing
print("first 3 letters:",text[0:3])
print("last 3 letters:",text[3:])
print("last 3 letters:",text[-3:])

#reverse string
print("reverse string:",text[::-1])

#using list with slicing and formatting
student=["dixit","jinal","raj","janvi","jiya","rutva"]

print("\n original list:",student)
print("\n first three student:",student[:3])

#loop
for student in student:
    print(f"welcome,{student}")

#length
    print("length of list:",len(student))

#checking element
    print("is jiya present?:","jiya" in student)

#nested list
    matrix=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
    print("matrix:",matrix)

#accessing element
    print("middle element:",matrix[1][1])

#string method
    message="python programming"

    print("uppercase:",message.upper())
    print("capitalized:",message.capitalize())
    print("replace:",message.replace("python","AI/ML"))
    print("split:",message.split())

#list method
number=[5,8,2,7,1]

number.sort()
print("sorted list:",number)

number.reverse()
print("reverse list:",number)

number.insert(1,100)
print("after insert:",number)
