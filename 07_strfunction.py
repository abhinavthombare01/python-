#String functions 
name = "Abhinav"
str = "Hello World"


#1) len() function
print(len(name)) #output = 7  #it will print the length of the string
print(len(str)) #output = 11  #it will print the length of the string spaces are also counted in length of the string
#2) endswith() function
print(name.endswith("av")) #output = True  #it will print True if the string ends with the specified value
#3) startswith() function
print(str.startswith("Hello")) #output = True  #it will print True if the string starts with the specified value
#4) capitalize() function
print(name.capitalize()) #output = "Abhinav"  #it will print the string with the first character capitalized
#5) upper() function
print(name.upper()) #output = "ABHINAV"  #it will print the string in uppercase
#6) lower() function
print(name.lower()) #output = "abhinav"  #it will print the string in lowercase
#7) find() function
print(name.find("a")) #output = 1  #it will print the index of the first occurrence of the specified value
#8) replace() function
print(name.replace("a", "A")) #output = "AbhinAv"  #it will replace all occurrences of the specified value with the new value
#9) count() function
print(name.count("a")) #output = 2  #it will print the number of occurrences of the specified value in the string



#Escpape sequence in string 
line = "abhi is a good boy \nbut not a bad boy also \n a great coder"
print(line) # output as it in the following way
#output = abhi is a good boy
#but not a  bad boy also
# a great coder
