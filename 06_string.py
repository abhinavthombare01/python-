#We can primirlly write a string in these three way 
a = "Hello World"  # using double quotes
b = 'Hello World'  # using single quotes
c = '''Hello World'''  # using triple quotes

#the index in string starts from 0 and goes to n-1 where n is the length of the string. 
#Example: 
name = "Abhinav"
nameshort = name[0:4] #output = "Abhi"  #slicing the string from index 0 to 3
print(nameshort)

#We can also use negative indexing or slicing in string which starts from -1 and goes to -n where n is the length of the string.
name1 = "Aman"
print (name1[-1:-5]) #output = "Aman"  #slicing the string from index -1 to -4

#we can also print like that 
print(name1[:4]) #output = "Aman"  #slicing the string from index 0 to 3
print(name1[0:]) #output = "Aman"  #slicing the string from index 0 to 3
#it also same as print(name1[0:4]) 

#SLICING WITH SKIP VALUE
name2 = "Abhinavt" #index values A=0, b=1, h=2, i=3, n=4, a=5, v=6, t=7 
print(name2[0:8:7]) #output = ""  #slicing the string from index 0 to 3 with skip value of 2
    