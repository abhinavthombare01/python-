#typecasting is the process of converting one data type to another data type in python.
#int() - converts to integer
#float() - converts to float
#str() - converts to string
#bool() - converts to boolean

#example: 
a = 5.5
b = type(a)
print(b) #output: <class 'float'>   
print("type :", b) #also we can print output like this answer is =  type : <class 'float'>   

# but if we put in double quotes then it will be a string
a = "5.5"
b = type(a)
print(b) #output: <class 'str'>

# now we convert using functions string to like int float str etc
a = "False"
b = bool(a) #converts string to boolean
b = type(b) 
print("type :", b) #output: <class 'bool'>