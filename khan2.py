#even or odd
a=int(input("Enter numbere:"))
if(a%2==0):
    print("Number is even")
else:
    print("Number is odd")  

 #grads according to the marks

marks=int(input("enter the marks:"))
if(marks>=90):
    print("grade is ->A")
elif(marks>=80 and marks<90):
    print("gradr is ->b")
elif(marks>=70 and marks<80):
    print("grade is -> c")
else:
    print("grade is ->d") 


#greatest of 4 numbers
 
a=int(input("enter the first no:"))
b=int(input("enter the second no:"))
c=int(input("enter the third no:"))
d=int(input("enter the fourth no:"))

if(a>b  and a>c and a>d):
    print("A is greater than all numbers")
elif(b>c and b>d):
    print("B is greater than all numbers")
elif(c>d):
    print (" C is greater tham all numbers") 
else:
    print("D is greater tahm all numbers") 

# type of the variable taken by the user and print the details
name=("fardeen khan")
age=21
weight=90.50
isstudent=True
print("Nmae:",name,type(name))
print("Age:",age,type(age))
print("Weight:",weight,type(weight))
print("isstudent:",isstudent,type(isstudent))



a=int(input("enter the no:"))
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")        

       