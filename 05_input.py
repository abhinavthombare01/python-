#when we print input like that in double quotes it will print the string as it is without any changes.
#example :
a = input("Enter Number First :")
b = input ("Enter Number Second :")

print("The First Number is :",a)
print("The Second Number is :",b)
print("The Sum of Two Numbers is :",a + b) 

#output:
# Enter Number First :2
# Enter Number Second :3
# The First Number is : 2
# The Second Number is : 3
# The Sum of Two Numbers is : 23


#now we will convert the input to integer using int() function and then add them.
a = int(input("Enter Number First :"))
b = int(input ("Enter Number Second :"))
print("The Sum of First and Second Numbers is :",a + b)

#output:
# Enter Number First :2
# Enter Number Second :3
# The Sum of First and Second Numbers is : 5

#now we solving problems for practice

# 1) Write a python program to find remainder when a number is divided by z.
a = int(input("Enter the number : "))
b = int(input("Enter the number to divide by and find remainder : "))
print("the Remainder is : ", a%b)
#output:
# Enter the number : 10
# Enter the number to divide by and find remainder : 3
# the Remainder is :  1
#for finding remainder we use "%" = (modulus) operator in python

# 2) use comparision operator to find out whether a number is greater than or equal to another number.

a = int(input("Enter the a number : "))
b = int(input("Enter the b number : "))
if a >= b:
    print("a is greater than b")
else:
    print("a is less than b")
if a == b:
    print("a is equal to b")


# 3) find average of three numbers entered by the user.
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

#to find average of three numbers this is the formula and their different ways to print average numbers.
average = (x + y + z) / 3  
print("The average of the three numbers is:", average) #or

print("The average of the three numbers is:", (x + y + z) / 3) #or

print("The average of the three numbers is:", sum([x, y, z]) / 3) 

