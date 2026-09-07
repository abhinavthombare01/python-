# ================================================================
# COMPLETE SET NOTES, REAL-WORLD EXAMPLES, AND PRACTICE
# ================================================================

# Set म्हणजे काय?
# Set म्हणजे unique values चा collection.
# Real world example: Website वर आलेल्या visitors चे duplicate IDs remove करणे.

visitor_ids = [101, 102, 101, 103, 102, 104]
unique_visitors = set(visitor_ids)
print("Unique visitors:", unique_visitors)
# Output: Unique visitors: {101, 102, 103, 104}
# Explanation: list ला set मध्ये convert केल्यावर duplicates आपोआप remove होतात.

# Set चे मुख्य points:
# 1. Set curly brackets {} मध्ये लिहितात.
# 2. Set duplicate values ठेवत नाही.
# 3. Set unordered असतो, म्हणून fixed index नसतो.
# 4. set[0] असे item access करता येत नाही.
# 5. Set mutable आहे, म्हणजे values add आणि remove करता येतात.


# 1. Set तयार करणे

skills = {"Python", "SQL", "Git"}
print("Skills:", skills)
# Output: Skills: {'Python', 'SQL', 'Git'}

# Duplicate value दिली तरी ती एकदाच राहते.
skills_with_duplicate = {"Python", "Python", "SQL"}
print("Unique skills:", skills_with_duplicate)
# Output: Unique skills: {'Python', 'SQL'}


# 2. Empty set
# {} हा empty dictionary आहे.
# Empty set तयार करण्यासाठी set() वापरा.

empty_set = set()
print("Empty set:", empty_set)
# Output: Empty set: set()


# 3. add()
# add() एक value set मध्ये add करतो.

skills.add("Docker")
print("After add:", skills)
# Output: After add: {'Python', 'SQL', 'Git', 'Docker'}


# 4. update()
# update() एकापेक्षा जास्त values add करतो.

skills.update(["Linux", "AWS"])
print("After update:", skills)
# Output: After update: {'Python', 'SQL', 'Git', 'Docker', 'Linux', 'AWS'}


# 5. remove() आणि discard()
# remove() value काढतो; value नसेल तर KeyError देतो.
# discard() value काढतो; value नसेल तरी error देत नाही.

skills.remove("Git")
skills.discard("Java")
print("After remove and discard:", skills)
# Output: After remove and discard: {'Python', 'SQL', 'Docker', 'Linux', 'AWS'}


# 6. Membership checking
# in वापरून set मध्ये value आहे का ते तपासता येते.

if "Python" in skills:
	print("Python skill is available")
# Output: Python skill is available


# 7. Set वर loop

for skill in skills:
	print("Skill:", skill)
# Note: Set unordered असल्यामुळे output चा order बदलू शकतो.
# Output: Skill: Python, SQL, Docker, Linux, AWS (order may change)


# 8. union()
# दोन sets मधील सर्व unique values मिळवतो.
# Real world: दोन courses मधील सर्व students शोधणे.

python_students = {"Ali", "Sara", "Abhi"}
java_students = {"Sara", "John", "Abhi"}

all_students = python_students.union(java_students)
print("All students:", all_students)
# Output: All students: {'Ali', 'Sara', 'Abhi', 'John'}

# | हा union() चा short operator आहे.
print("All students:", python_students | java_students)
# Output: All students: {'Ali', 'Sara', 'Abhi', 'John'}


# 9. intersection()
# दोन्ही sets मध्ये असणाऱ्या common values मिळवतो.

common_students = python_students.intersection(java_students)
print("Students in both courses:", common_students)
# Output: Students in both courses: {'Sara', 'Abhi'}

# & हा intersection() चा short operator आहे.
print("Students in both courses:", python_students & java_students)
# Output: Students in both courses: {'Sara', 'Abhi'}


# 10. difference()
# पहिल्या set मध्ये आहेत पण दुसऱ्या set मध्ये नाहीत अशा values मिळवतो.

only_python = python_students.difference(java_students)
print("Only Python students:", only_python)
# Output: Only Python students: {'Ali'}

# - हा difference() चा short operator आहे.
print("Only Java students:", java_students - python_students)
# Output: Only Java students: {'John'}


# 11. symmetric_difference()
# फक्त एका set मध्ये असणाऱ्या values मिळवतो; common values येत नाहीत.

different_students = python_students.symmetric_difference(java_students)
print("Students in only one course:", different_students)
# Output: Students in only one course: {'Ali', 'John'}

# ^ हा symmetric_difference() चा short operator आहे.
print("Students in only one course:", python_students ^ java_students)
# Output: Students in only one course: {'Ali', 'John'}


# 12. Set practical example: product tags
# दोन products चे tags compare करून common features शोधणे.

phone_tags = {"electronics", "mobile", "5G", "android"}
tablet_tags = {"electronics", "tablet", "5G", "android"}

print("Common tags:", phone_tags & tablet_tags)
# Output: Common tags: {'electronics', '5G', 'android'}
print("All tags:", phone_tags | tablet_tags)
# Output: All tags: {'electronics', 'mobile', '5G', 'android', 'tablet'}
print("Only phone tags:", phone_tags - tablet_tags)
# Output: Only phone tags: {'mobile'}


# ================================================================
# PRACTICE QUESTIONS WITH ANSWERS
# ================================================================

# Question 1:
# fruits नावाचा set तयार करा: apple, banana, mango.
# Answer:
practice_fruits = {"apple", "banana", "mango"}
print("Practice 1:", practice_fruits)
# Output: Practice 1: {'apple', 'banana', 'mango'}

# Question 2:
# orange add करा.
# Answer:
practice_fruits.add("orange")
print("Practice 2:", practice_fruits)
# Output: Practice 2: {'apple', 'banana', 'mango', 'orange'}

# Question 3:
# apple पुन्हा add करा आणि result पाहा.
# Answer:
practice_fruits.add("apple")
print("Practice 3:", practice_fruits)
# Output: Practice 3: {'apple', 'banana', 'mango', 'orange'}
# Explanation: apple duplicate असल्यामुळे set मध्ये दुसऱ्यांदा add होत नाही.

# Question 4:
# banana remove करा.
# Answer:
practice_fruits.remove("banana")
print("Practice 4:", practice_fruits)
# Output: Practice 4: {'apple', 'mango', 'orange'}

# Question 5:
# mango exists आहे का check करा.
# Answer:
print("Practice 5:", "mango" in practice_fruits)
# Output: Practice 5: True
# Explanation: in True किंवा False return करतो.

# Question 6:
# दोन number sets चा union आणि intersection शोधा.
# Answer:
first_numbers = {1, 2, 3, 4}
second_numbers = {3, 4, 5, 6}
print("Practice 6 union:", first_numbers | second_numbers)
# Output: Practice 6 union: {1, 2, 3, 4, 5, 6}
print("Practice 6 intersection:", first_numbers & second_numbers)
# Output: Practice 6 intersection: {3, 4}

# Question 7:
# List मधून duplicate marks remove करा.
# Answer:
student_marks = [80, 90, 80, 75, 90, 95]
unique_marks = set(student_marks)
print("Practice 7:", unique_marks)
# Output: Practice 7: {80, 90, 75, 95}
# Explanation: set() duplicate marks एकदाच ठेवतो.


# लक्षात ठेवा:
# set()                       -> empty set किंवा conversion
# add(value)                 -> एक value add
# update(values)             -> अनेक values add
# remove(value)              -> value remove; missing value वर error
# discard(value)             -> value remove; missing value वर error नाही
# set1.union(set2)           -> दोन्ही sets मधील सर्व unique values
# set1.intersection(set2)    -> common values
# set1.difference(set2)      -> फक्त set1 मधील values
# set1.symmetric_difference(set2) -> फक्त एका set मधील values
# value in set               -> value exists का ते check