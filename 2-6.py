#(1) find second largest elements
arr = [12,45,79,89,67]
arr.sort()
print(arr)

print("second largest:,arr[-2]")

#(2) remove publicate elements
arr = [10,20,30,10,30,40,20]
unique=[]

for i in arr:
    if i not in unique:
        unique.append(i)

print("array:",unique)

#(3) frequency of each element
arr = [10,20,30,10,30,40,10]

for i in set(arr):
    print(i , "appers" , arr.count(i) , "times")

#find missing number
arr = [1,2,3,5,6]
n=6

expected = n*(n+1)//2
actual = sum(arr)

print("missing number:",expected-actual)

#merge and sort two arrays
arr1=[10,30,50]
arr2=[20,40,60]

merged=arr1+arr2

print(merged)
merged.sort()
print(merged)

#kandanes algorithm (maximum subarray sum)
arr = [-2,1,-3,4,-1,2,1,-5,4]
current = maximum = arr[0]

for i in arr[1:]:
    current=max(i,current+i)
    maximum=max(maximum,current)

print("maximum sum",maximum)

#2D Array
#Addition of two matrix
A = [
    [1,2],
    [3,4]
    ]
B = [
    [4,5],
    [6,7]
    ]
result = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j]+B[i][j])
    result.append(row)

for row in result:
    print(row)

#find largest element in each row
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ]
for row in matrix:
    print("largest:",max(row))
        

