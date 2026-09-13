fruits=[
    "apple",
    "banana",
    "orange",
    "orange"
]
# Ordered
print(fruits)

# Changeable
fruits[0]="sabe"
print(fruits)

# Allow duplicate values
print(fruits)

# Able to contain different data types
fruits.append(20)
print(fruits)

# Indexed starting from 0
# fruits[0]
# fruits[1]
# fruits[2]
# fruits[3]
# fruits[4]
# fruits[5]


# Accessing the elements in reverse order
# from 0 --> n-1
# from -n <-- -1
print(fruits[0],fruits[-1])
print(fruits[1],fruits[-3])
print(fruits[2],fruits[-3])
print(fruits[3],fruits[-4])
print(fruits[4],fruits[-5])

# Traceback (most recent call last):
#   File "c:\Users\patid\OneDrive\Desktop\Python\main.py", line 83, in <module>
#     fruits[5]
# IndexError: list index out of range


list=[]
# methods in list

# append(data) ->add ele at end
list.append(10)
list.append(20)

print(list)

# insert(index,data) -> add ele at specific index
list.insert(1,200)
print(list)

# Adds multiple items:
list.extend([1000,90100])
print(list)

# remove item -> It raises an error if the value does not exist.

# list.remove("orange")

# Safer version:
if 200 in list:
    list.remove(200)

# pop -> Removes and returns an item:
# remove element at 0th index
deletedEle=list.pop(0)
print(deletedEle)
print(list)

del list[0]

list.extend([10000,200000,98882])
print(list)
# delete a range
del list[0:1]

# Delete the entire list variable:
del fruits

print(list)

# clear() -> Removes all items:

# List Length
print(len(list))


# check items is present inside list or not
if 200 in list:
    print(200,"Yes")
else:
    print(200,"Not")   

if 300 not in list:
    print("No")

# spliceing list
# list[strat:stop:end]
print(list) #[90100, 10000, 200000, 98882]
print(list[0:2]) # [90100, 10000]
print(list[:3])
print(list[0:])
print(list[0:2:3]) 
print(list[:])
print(list[0:3:2])

# looping  through list
for i in list:
    print(i)

# with index
for index,i in enumerate(list):
    print(index,i)

for index,i in enumerate(list, start=1):
    print(index,i)

list.sort()
print(list)

# reverse order
list.sort(reverse=True)
print(list)

# Creates a new sorted list:
new_number=sorted(list)
print(list)
print(new_number)

# print(fruits)

print("------------------------")

# sort string by length
names=["vinay","raj","vinayak","raghu"]
print(names)
sortedNames=sorted(names)
print(sortedNames)

sortedNamesReverse=sorted(names,reverse=True)
print(sortedNamesReverse)
names.reverse()
print(names)

# Finding Values
print(numbers.index(3))  # 3

# copy list
original = [1, 2, 3]
copy = original
copy.append(4)
print(original)
print(copy)


# copy list
o=[1,2,3]
c=o.copy()

o.append(910)
c.append(1000)
print("o",o)
print("c",c)

# list operator
li1=[1,2,3]
li2=[4,5,6]
li3=li1+li2
print(li1+li2)

# repeating list
zeros=[0]
zeros=zeros*5
print(zeros)


# useful build in function
no=[1,2,3,4,5]
print(len(no))  # 5
print(min(no))  # 1
print(max(no))  # 5
print(sum(no))  # 15

# short way to create list
square=[n*n for n in range(1,6)]
print(square)
# With a condition:

evenNo=[
    n 
    for n in range(1,6)
    if n%2==0 #condition
]
print(evenNo)


names = ["alice", "bob", "charlie"]

uppercase_names = [name.upper() for name in names]
print(uppercase_names)


# labels
labels =[
    "even" if number % 2 == 0 else "odd"
    for number in range(1, 6)
]

print(labels)

# nested list
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)

for row in matrix:
    for col in row:
        print(col)

# Unpacking Lists
colors = ["red", "green", "blue","yellow"]
first,*second,third=colors
print(first)
print(second)
print(third)


print("--------------------------------------------")
groceries=["bread"]

groceries.append("milk")
groceries.append("rice")

groceries.insert(1,"apple")
print(groceries)

if "bread" in groceries:
    groceries.remove("bread")

print(groceries)

groceries.pop(-1);

print(groceries)

print(len(groceries))

if "milk" in groceries:
    print("Yes")


groceries.sort(reverse=True)
print(groceries)

for ele in groceries:
    print(ele)