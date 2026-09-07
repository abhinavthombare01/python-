"""Python conditional expressions and statements."""

# A condition produces either True or False.
age = 20

if age >= 18:
	print("You can vote")
else:
	print("You cannot vote yet")

# Use elif when there are several possible conditions.
marks = 76

if marks >= 90:
	grade = "A"
elif marks >= 75:
	grade = "B"
elif marks >= 50:
	grade = "C"
else:
	grade = "Fail"

print("Grade:", grade)

# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not
temperature = 28
is_sunny = True

if temperature > 25 and is_sunny:
	print("It is a good day for a walk")

# Conditional expression: value_if_true if condition else value_if_false
number = 7
result = "even" if number % 2 == 0 else "odd"
print(number, "is", result)
