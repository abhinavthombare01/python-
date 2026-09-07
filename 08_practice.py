# 1) Wirte a python programe to display a user entered a name followed by Good Afternoon using input() function

name = input("Enter your name: ") #taking input from user
print("Good Afternoon," + name)

#also we can write using f-string
name1 = input("Enter your name: ") #taking input from user
print(f"Good Morning, {name1}") #using f-string to print the name

#2) Write a python program to add two numbers using input() function
num1 = int(input("Enter First number:"))
num2 = int(input("Enter Second number:"))
print(num1+num2)

#3) write a program to fill in letter template given below with name and date 
# letter ='''
#   Dear <|Name|>
#   You are selected !
#   <|Date|>
#   ''' 

letter =''' Dear <|Name|>,
 You are selected!
 <|Date|> ''' 
print (letter.replace("<|Name|>","Abhi").replace("<|Date|>","22 April 2005"))
#this is how replace() function is also used in example

#Write a program to detect the double space

line1 = ("my name is abhi  i am student")
print(line1.find("  ")) #this function used for detect space
print(line1.replace("  "," "))

