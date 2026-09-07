# chapter-4
#List creation and conversion
list()              # Create empty list
list("abc")         # Convert to list: ['a', 'b', 'c']
list(range(5))      # [0, 1, 2, 3, 4]
list((1, 2, 3))     # Convert tuple to list

#Adding Elements in the list
fruits = ["apple", "banana"]

fruits.append("orange")    # Add to end
# fruits: ["apple", "banana", "orange"]
print(fruits)

fruits.extend(["mango", "pear"]) # Add multiple items
# fruits: ["apple", "grape", "banana", "orange", "mango", "pear"]
print(fruits)

fruits.pop()           # Remove last & return it: "pear"
print(fruits)
fruits.pop(0)          # Remove at index 0: "apple"
fruits.remove("grape") # Remove by value
fruits.clear()         # Remove all items
del fruits[0]          # Delete by index

#python list are containner 
items = ["apple" , "orrange" , 14.99 , 80 ]
print(items) 
print(items[0:2])
items.append("Banana")  # .append() function adds string in list
print(items) 

#.sort() it sorts the lists for example
#list also put in square bracket in python
l1 = [12, 18, 14, 15]
l1.sort()  #sort in asscending order
l1.reverse() #sort in decending order
l1.insert(2 , 13)  #insert 13 on second position of list

l1.pop(3) #delete that perticular integer or string from the list.
print(l1) 


#PROBLRM 1 : write a program to store five fruits entered by the user
fruits = []
f1 = input("Enter fruit name :")
fruits.append(f1)

f2 = input("Enter fruit name :")
fruits.append(f2)

f3 = input("Enter fruit name :")
fruits.append(f3)

f4 = input("Enter fruit name :")
fruits.append(f4)

f5 = input("Enter fruit name :")
fruits.append(f5)

print(fruits)

#write a program to accept marks of 6 student and display yhem in sorted manner 

marks = []
m1 = int(input("Enter marks here :"))
marks.append(m1)
m2 = int(input("Enter marks here :"))
marks.append(m2)
m3 = int(input("Enter marks here :"))
marks.append(m3)
m4 = int(input("Enter marks here :"))
marks.append(m4)
m5 = int(input("Enter marks here :"))
marks.append(m5)

marks.sort()
print(marks)


#wirte a program to sum a list of 5 numbers

numbers = [ 1, 2, 3, 4, 5]
print(sum(numbers))


# ================================================================
# COMPLETE LIST NOTES, REAL-WORLD EXAMPLES, AND PRACTICE
# ================================================================

# List म्हणजे काय?
# List म्हणजे एकाच variable मध्ये अनेक values store करण्याचा container.
# Real world example: Shopping cart मध्ये अनेक products store करणे.

cart = ["laptop", "mouse", "keyboard"]
print("Shopping cart:", cart)

# List चे मुख्य points:
# 1. List square brackets [] मध्ये लिहितात.
# 2. List ordered असते, म्हणून items चा order जपला जातो.
# 3. Index 0 पासून सुरू होतो.
# 4. List mutable असते, म्हणजे list बदलता येते.
# 5. Duplicate values चालतात.
# 6. वेगवेगळ्या data types एकाच list मध्ये ठेवता येतात.

different_items = ["apple", 25, 12.5, True]
print("Different data types:", different_items)


# 1. Indexing
# Index वापरून list मधील एक item access करता येतो.

fruits = ["apple", "banana", "mango"]
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

# Index positions:
# apple = 0, banana = 1, mango = 2


# 2. Slicing
# List मधील काही items मिळवण्यासाठी slicing वापरतात.

all_fruits = ["apple", "banana", "mango", "orange"]
print("First two fruits:", all_fruits[0:2])
print("Last two fruits:", all_fruits[-2:])
# Explanation: 0:2 मध्ये index 0 घेतला जातो, पण index 2 घेतला जात नाही.


# 3. append()
# append() एक item list च्या शेवटी add करतो.

cart = ["laptop", "mouse"]
cart.append("keyboard")
print("After append:", cart)


# 4. extend()
# extend() दुसऱ्या collection मधील अनेक items add करतो.

cart.extend(["USB cable", "headphones"])
print("After extend:", cart)


# 5. insert()
# insert(index, value) दिलेल्या position वर item add करतो.

cart.insert(1, "monitor")
print("After insert:", cart)
# Explanation: monitor index 1 वर add झाला आणि बाकीचे items पुढे shift झाले.


# 6. remove()
# remove(value) value च्या नावाने पहिला matching item काढतो.

cart.remove("USB cable")
print("After remove:", cart)
# Explanation: दिलेली value list मध्ये नसेल तर remove() error देतो.


# 7. pop()
# pop(index) index वरील item काढतो आणि तो item return करतो.

removed_item = cart.pop(1)
print("Removed item:", removed_item)
print("After pop:", cart)

# Index न दिल्यास pop() शेवटचा item काढतो.
last_item = cart.pop()
print("Last removed item:", last_item)


# 8. sort()
# sort() numbers किंवा strings ascending order मध्ये arrange करतो.

delivery_times = [5, 2, 7, 3]
delivery_times.sort()
print("Ascending order:", delivery_times)

# Descending order साठी reverse=True वापरतात.
delivery_times.sort(reverse=True)
print("Descending order:", delivery_times)


# 9. reverse()
# reverse() list मधील current order उलटा करतो.

numbers = [1, 2, 3, 4]
numbers.reverse()
print("Reversed list:", numbers)


# 10. len() आणि sum()
# len() list मधील items ची संख्या सांगतो.
# sum() numbers ची बेरीज करतो.

marks = [80, 90, 75, 85]
print("Number of subjects:", len(marks))
print("Total marks:", sum(marks))
print("Average marks:", sum(marks) / len(marks))


# 11. List मध्ये value आहे का हे check करणे

subjects = ["Python", "Java", "C++"]
if "Python" in subjects:
	print("Python is present")


# 12. List वर loop
# Loop प्रत्येक item एक-एक करून वाचतो.

for subject in subjects:
	print("Subject:", subject)


# 13. Real-world example: student marks
# Student चे marks list मध्ये store करून total, average आणि result काढणे.

student_marks = [80, 65, 72, 90, 55]
total_marks = sum(student_marks)
average_marks = total_marks / len(student_marks)

print("Student total:", total_marks)
print("Student average:", average_marks)

if average_marks >= 40:
	print("Student passed")
else:
	print("Student failed")


# 14. Real-world example: shopping cart

shopping_cart = ["phone", "cover"]
shopping_cart.append("charger")
shopping_cart.remove("cover")
print("Final shopping cart:", shopping_cart)
# Explanation: Product add करण्यासाठी append() आणि remove करण्यासाठी remove().


# ================================================================
# PRACTICE QUESTIONS WITH ANSWERS
# ================================================================

# Question 1:
# subjects = ["Python", "Java", "C++"]
# HTML शेवटी add करा.
# Answer:
practice_subjects = ["Python", "Java", "C++"]
practice_subjects.append("HTML")
print("Practice 1:", practice_subjects)

# Question 2:
# JavaScript index 1 वर add करा.
# Answer:
practice_subjects.insert(1, "JavaScript")
print("Practice 2:", practice_subjects)

# Question 3:
# C++ remove करा.
# Answer:
practice_subjects.remove("C++")
print("Practice 3:", practice_subjects)

# Question 4:
# दुसरा subject print करा.
# Answer:
print("Practice 4:", practice_subjects[1])
# Explanation: दुसऱ्या item चा index 1 असतो.

# Question 5:
# Numbers sort करून smallest आणि largest number print करा.
# Answer:
practice_numbers = [45, 12, 89, 34, 7]
practice_numbers.sort()
print("Practice 5 sorted:", practice_numbers)
print("Smallest:", practice_numbers[0])
print("Largest:", practice_numbers[-1])

# Question 6:
# Five numbers ची बेरीज आणि average काढा.
# Answer:
five_numbers = [10, 20, 30, 40, 50]
print("Practice 6 sum:", sum(five_numbers))
print("Practice 6 average:", sum(five_numbers) / len(five_numbers))


# लक्षात ठेवा:
# append(value)       -> शेवटी एक item add
# extend(values)      -> अनेक items add
# insert(index,value) -> specific position वर item add
# remove(value)       -> value वापरून item remove
# pop(index)          -> index वापरून item remove
# sort()              -> ascending order
# reverse()           -> order उलटा
# len(list)           -> items ची संख्या
# sum(list)           -> numbers ची बेरीज

