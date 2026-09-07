#Tuples are immutable sequences in Python—ordered collections of elements that cannot be changed after creation.

''' Key Characteristics
Immutable: Cannot add, remove, or modify elements
Ordered: Elements maintain their position
Indexable: Access elements by index (0-based)
Iterable: Can loop through them
Heterogeneous: Can contain different data types

# Tuple vs List
Feature:	Tuple	              List
Syntax:	  (1, 2, 3)	            [1, 2, 3]
Ordered:	✅	                  ✅
Mutable:	❌	                  ✅
Duplicates: ✅                     ✅
Indexing	✅                     ✅
Methods	    Few	                   Many
Performance:Generally faster Generally slower

Simple rule to remember

List → data can change
Tuple → data should remain fixed
 '''

# Basic syntax
empty_tuple = ()
single_element = (5,)  # Note: comma required!
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

# Unpacking
a, b, c = (10, 20, 30)

print(single_element)

# Indexing and slicing
tup = (10, 20, 30, 40, 50)
print(tup[0])      # 10
print(tup[-1])     # 50
print(tup[1:3])    # (20, 30)

# Length and membership
len(tup)           # 5
20 in tup          # True

# Tuple Methods
tup.count(20)      # 1 (how many times 20 appears)
tup.index(30)      # 2 (index of first 30)

# Concatenation and repetition
t1 = (1, 2)
t2 = (3, 4)
combined = t1 + t2  # (1, 2, 3, 4)
repeated = t1 * 3   # (1, 2, 1, 2, 1, 2)

# Iteration
for item in tup:
    print(item)


#Named Tuple (Modern best practice)

from collections import namedtuple
#more readable and maintainable 
User = namedtuple('User',['id','name','email','verified'])
user = User(101,"Abhi Thombare","abhinavthombare22@gmail.com",True)
print(user) 

name1 = user.count("Abhi Thombare")
print(name1)

# List
marks = [80, 90, 75]
marks[0] = 85       # Allowed

# Tuple
coordinates = (18.52, 73.85)
# coordinates[0] = 20   # Not allowed

#problem 2 : wirte a program to count the numbers of zeros in following tupple
# a = (2, 0, 3, 0, 5, 0)

a = (2, 0, 3, 0, 5, 0)
n = a.count(a)