#empty list
users = []

#create
user1 = {
    'id':1,
    'name':'alice',
    'email':'alice@gmail.com'
    }
user2 = {
    'id':2,
    'name':'zeel',
    'email':'zeel@gmail.com'
    }
user3 = {
    'id':3,
    'name':'karan',
    'email':'karan@gmail.com'
    }

#add users
users.append(user1)
users.append(user2)
users.append(user3)

print("user added successfully!")


#read
print("\n all users:")

for user in users:
    print(user)

#search
search_id=2
print("\n searching user:")

for user in users:
    if user ['id'] == search_id:
        print("user founf:",user)


#update
print("\n updating user email....")
for user in users:
    if user['id'] == 2:
        user['email']='zeel@example.com'

print("user updated!")
print(user)


#delete
print("\n deleting users....")
for user in users:

    if user['id'] == 1:
        users.remove(user)
        break
print("user deleted!")


#count users
print ("\n total users:,len",len(users))

#check email exists
check_email ='zeel@gmail.com'

found = False

for user in users:
 if user['email'] == check_email:
       found = True

if found:
  print("email exists")
else:
  print("email not found")


#sort user by name
  sorted_users = sorted(users ,key = lambda x : x['name'])

  print('\n sortes users:')
  for user in sorted_users:
      print(user)


#final user list
print("\n =============final users=============")
for user in users:
     print(f"""
ID:{user['id']}
Name :{user['name']}
Email:{user['email']}
""")


#type casting constructor
#list()--->tuple()

a=[1,2,3,4]
b=tuple(a)
c=set(a)

print(b)
print(c)


#del keyword
#used to delete variable,list element,disctionary keys,etc.....

x=[10,20,30]
del x[1]
print(x)

person={'name':'vishva','age':30}
del person['age']
print(person)
     
