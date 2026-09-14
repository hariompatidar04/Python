empty=()
number=(1,2,3)
mixed=("Alice",25,True)
nested=((1,2),(3,4))

print(type(empty))
print(type(number))
print(type(mixed))
print(type(nested))




# A tuple with one item requires a comma:
one_item=(10)
print(type(one_item))#int
one_item=(10,)
print(type(one_item))#tupple


colors = ("red", "green", "blue")
#          0(-3)  1(-2)    2(-1)

print(colors[0])   # red
print(colors[-1])  # blue



numbers = (0, 1, 2, 3, 4, 5)
print(numbers[1:4])  # (1, 2, 3)
print(numbers[:3])   # (0, 1, 2)
print(numbers[3:])   # (3, 4, 5)
print(numbers[::-1]) # (5, 4, 3, 2, 1, 0)


#Tuples Are Immutable

coordinates = (10, 20)
print(coordinates)
# coordinates[0] = 50  # TypeError

# To create a changed tuple
coordinates=(50,coordinates[0])
print(coordinates)

# Tuple Methods
# count()
number=(1,2,3,4,5,3)
print(number.count(3));

# index()-> returns the position of the first matching item.
print(number.index(3))

fruits = ("apple", "banana", "orange")


#  Tuple Length and Membership
print(len(fruits))             # 3
print("apple" in fruits)       # True
print("mango" not in fruits)   # True


person=("Vinay",22,"Python","50000.0","17-12-2004")
name,age,language,*oth=person
print(name)
print(age)
print(language)
print(oth)


# swapping an element

a=10
print(a)
b=20
print(b)
a,b=b,a
print(a)
print(b)


#  Tuple Packing
# Python automatically creates a tuple when values are separated by commas:

person = "Alice", 25, "Python"
print(person)
print(type(person))  # tuple
# Parentheses are optional, but using them improves readability.

# list->tupple
num_list=[1,2,3,4]
print(type(num_list))
print(num_list)

num_tupple=tuple(num_list)
print(type(num_tupple))
print(num_tupple)

# tupple->list

num_li=list(num_tupple)
print(type(num_li))
print(num_li)

# joining tuple
first=(1,2)
second=(3,4)
third=first+second
print(type(third))
print(third)


# loop through a tuple
fruits=("apple","banana","orange")
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)

    # nested tuple
    matrix=((1,2,3),(4,5,6),(7,8,9))
    for row in matrix:
        for col in row:
          print(col)

data=("Ram","Shyam",[1,2,3])
# data[0]="Vikas" #Type Error
# data[2]="Vikas" #Type Error
data[2].append(5)# list is mutable so i am not getting any error
print(data)


# Tuple Comparisons
# Tuples are compared item by item:
# Order matters:

print((1, 2) == (1, 2))  # True
print((1, 2) == (1, 2))  # False
print((1, 2) < (2, 1))   # True


# Sorting Tuples

numbers = (5, 2, 8, 1)
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 5, 8]
# Convert the result back to a tuple:
sorted_numbers = tuple(sorted(numbers))

# Type Hints
user: tuple[str, int] = ("Alice", 25)
# This means the tuple contains a string followed by an integer.

# For a tuple containing any number of integer
numbers: tuple[int, ...] = (1, 2, 3, 4)









