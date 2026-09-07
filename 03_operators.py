# arithmetic operators

a = 2
b = 3
c = a + b
#print the result techniques also
print (c)     #output: 5
print ("answer :" + str(c)) #output: 5
print ("answer :" + str(a - b)) #output: -1
print (c * 2) #output: 10


#assignment operators

a = 5-1 
print(a) #output: 4

b = 3 
b += 2 #increment the value of b by 2 and then assign the result back to b
print(b) #output: 5

c = 10
c -= 3 #decrement the value of c by 3 and then assign the result back to c
print(c) #output: 7 

d = 4
d *= 2 #multiply the value of d by 2 and then assign the result back to d
print(d) #output: 8

e = 16
e /= 2 #divide the value of e by 2 and then assign the result back to e
print(e) #output: 8.0


# =, +=, -=, *=, /=, %=, **=, //= are the assignment operators in python 
# and remember that they are used to assign values to variables and perform operations on them.

#comparision operators
a = 5   #assign 5 to a ,= is the assignment operator but
5 == 5  #this is the comparison operator which checks if 5 is equal to 5 or not and returns True or False
a <= b  # this checks if a is less than or equal to b and returns True or False
a >= b  # this checks if a is greater than or equal to b and returns True or False
a != b  # this checks if a is not equal to b and returns True or False

#logical operators

# #or operator statement 
# true or false is true 
# true or true is true
# false or false is false
# false or true is true 

#Exam
a= True 
b= False
print(a or b) #output: True
print(a and b) #output: False
print(not a) #output: False
print(True and True) #output: True


#example:
#Truth table for or operator
True or True = True
True or False = True
False or True = True
False or False = False
#Truth table for and operator
True and True = True
True and False = False
False and True = False
False and False = False
#Truth table for not operator
not True = False
not False = True
not (True and False) = True
not (False or True) = False
not (True or False) = False
not (False and True) = True

