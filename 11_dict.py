"""
PYTHON DICTIONARY NOTES
=======================

1. What is a dictionary?
-------------------------
A dictionary stores data in KEY-VALUE pairs.

    key        value
    "name"  : "Ali"

Keys are used to find values. A dictionary is useful when every value has
a meaningful name. For example, a person's name, age, and city.

Important points:
- A dictionary is written with curly brackets: { }
- Every pair has a key and a value, separated by a colon (:).
- Different pairs are separated by commas.
- Keys must be unique.
- A dictionary can be changed after it is created, so it is mutable.
"""

# 2. Creating a dictionary
# ------------------------
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}

print("Student:", student)
print(type (student))

# 3. Accessing values
# -------------------
# Use the key inside square brackets to get its value.
print("Name:", student["name"])
print("Age:", student["age"])

# If a key does not exist, square brackets give a KeyError.
# print(student["email"])

# get() is safer when a key may not exist.
print("Email:", student.get("email"))
print("Email:", student.get("email", "abhi22@gmail.com"))
#syntax : dictionary.get(key, default_value)
'''If the key exists, it returns its value.
If the key does not exist, it returns the default value.
also default value nasel tr none output yett .
It prevents KeyError.
It does not add the missing key automatically.'''

# 4. Adding and changing items
# ----------------------------
student["email"] = "ali@example.com"  # Adds a new item
student["age"] = 21                    # Changes an existing value
print("After adding and changing:", student)


# 5. Common dictionary methods
# ----------------------------
# keys() returns all keys.
print("Keys:", student.keys())

# values() returns all values.
print("Values:", student.values())

# items() returns all key-value pairs.
print("Items:", student.items())

# update() adds new items or changes existing items.
student.update({"city": "Lahore", "age": 22})
print("After update:", student)
student.update({"PinNo" : 123212})
print("after update :",student)

# pop() method removes the item with the given key and its value.
removed_email = student.pop("email")
print("Removed email:", removed_email)
print("After pop:", student)

# popitem() removes and returns the last inserted key-value pair.
last_item = student.popitem()
print("Removed last item:", last_item)

# copy() creates a separate copy of the dictionary.
student_copy = student.copy()
print("Copy:", student_copy)

# clear() removes every item from a dictionary.
student_copy.clear()
print("After clear:", student_copy)


# 6. Checking whether a key exists
# --------------------------------
if "name" in student:
    print("The name key exists")

if "phone" not in student:
    print("The phone key does not exist")


# 7. Looping through a dictionary
# -------------------------------
for key in student:
    print("Key:", key)

for value in student.values():
    print("Value:", value)

for key, value in student.items():
    print(key, "=", value)


# 8. Nested dictionaries
# -----------------------
# A value can itself be another dictionary.
classroom = {
    "student1": {"name": "Ali", "marks": 85},
    "student2": {"name": "Sara", "marks": 92}
}



print("Student 1 name:", classroom["student1"]["name"])
print("Student 2 marks:", classroom["student2"]["marks"])


# 9. Dictionary comprehension
# ---------------------------
# This creates a dictionary in one short expression.
squares = {number: number * number for number in range(1, 6)}
print("Squares:", squares)


# 10. Practical example: count letters in a word
# -----------------------------------------------
word = "banana"
letter_count = {}

for letter in word:
    # get(letter, 0) means: use the current count, or 0 if it is new.
    letter_count[letter] = letter_count.get(letter, 0) + 1

print("Letter count:", letter_count)


"""
PRACTICE
--------
Create this dictionary:

book = {
    "title": "Python Basics",
    "author": "John",
    "price": 500
}


Tasks:
1. Print the title.
2. Change the price to 600.
3. Add a "pages" key with the value 250.
4. Print all keys and values.
5. Remove the author.
6. Print the final dictionary.
"""
book = {
    "title": "Python Basics",
    "author": "John",
    "price": 500
}

# 1. Print the title
print(book["title"])

# 2. Change the price
book["price"] = 600

# 3. Add pages
book["pages"] = 250

# 4. Print all keys and values
for key, value in book.items():
    print(key, "=", value)

# 5. Remove the author
book.pop("author")

# 6. Print the final dictionary
print(book)
#A dictionary stores data as key-value pairs.

''' "name", "age", and "course" are keys.
"Abhi", 21, and "Python" are values.
Keys must be unique.
Dictionaries are mutable, meaning they can be changed. '''

# example 
student = {
    "name" : "abhi",
    "age" : 21,
    "cource" : "pyhton"
}
print (student) 
#output : {'name': 'Ali', 'age': 20, 'course': 'Python'}

#also we can access values using key
print(student["name"])
print(student["age"])

#how to count  sales using get() method
sales ={}
items = ["laptop","mouse","laptop","macos","macos","laptop"]
for count_items in items :
    sales[count_items] = sales.get(count_items,0)+1
print(sales)
