#program with *args with UDF function
def filter_args(*args):
    string=()
    numbers=()

    for item in args:
        if type(item)==str:
            string += (item,)
        elif type(item) in (int,float):
                numbers += (item,)

                return string, numbers

result = filter_args("apple",10,"orange",23,3.5,"manan")

print("string:", result[0])
print("numbrers",result[1])

#using 1D array using loop
list_1=[10,20,30,40,50]
for item in list_1:
    print(item)

list_2=[10,45,20,78,89]
total=0

for item in list_2:
    total+=item
    print(total)

print("array of sum",sum(list_2))

#write a program to find the length od a 1D array without using built-in-function
arr=[]
size=int(input("enter array size:"))

for item in range(size):
    value=int(input(f"a[{item}]="))
    arr.append(value)

count=0

for i in arr:
    count += 1

print("length of array:",count)

#write a program to find average of 1D array without using any built-in method
arr=[]
size=int(input("enter array sizes"))

for item in range(size):
    value=int(input(f"a[{item}]="))
    arr.append(value)

sums=0
count=0

for i in arr:
    sums += i
    count += 1

average=sums/count

print("average of array",average)

#writw a program to perform addition of two 1D array and store in another array
arr1=[]
arr2=[]
arr3=[]

size=int(input("enter array size:"))

print("enter arr 1 elements:")
for item in range(size):
    value=int(input(f"a[{i}]="))
    arr1.append(value)

print("enter arr2 elemrnts:")
for item in range(size):
    value=int(input(f"a[{i}]"))
    arr2.append(value)

for i in range(size):
    arr3.append(arr1[i]+arr2[i])

print("array 3:",arr3)

#write a program an array of numbers from 1 to 10
arr=[]

for i in range(1,11):
    arr.append(i*2)

print(arr)

#take user input for a number and check if it exists in the array

arr=[10,20,40,50,80]

num=int(input("enter number to search:"))
found=False

for i in range(len(arr)):
    if arr [i] == num:
        print("found at index:",i)
        found=true
        break

if found == False:
    print("not found")

#print all even numbers from the array
arr=[]

size=int(input("even size of array:"))

for i in range(size):
    value=int(input(f"a[{i}]="))
    arr.append(value)

print("even number:")

for i in arr:
    if i % 2 == 0:
        print(i)

for i in arr:
    if i % 2 == 0:
        print(i)

print("odd number:")

for i in arr:
    if i % 2 !=0:
        print(i)
'''
'''#print the first,middle and last element in array
arr=[10,20,30,40,50,60]

print("first element:",arr[0])
print("last element:",arr[-1])

middle=len(arr)//2

print("middle element:",arr[middle])

#2D array
arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ]
print(arr)

#arr[row][column]
print(arr[0][1])
print(arr[2][2])

#take input in 2D array
arr=[]

rows=int(input("enter rows:"))
columns=int(input("enter columns:"))

for i in range(rows):
    row=[]
for j in range(columns):
    value=int(input(f"[{i}][{j}]"))
    row.append(value)
    arr.append(row)

print(arr)


#print 2D array using nsted loop
arr=[
    [1,2],
    [3,4]
    ]
total=0

for i in arr:
    for j in i:
        total+=j

print("total:",total)

#sorting collection datatype
#sort()method
numbers=[1,8,5,2,9,4]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

#sorting string list

fruits=["mango","apple","banana","orange"]

fruits.sort()
print(fruits)
