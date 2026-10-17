#same type of the list and its type(list is the mutetable)

marks=[56,98,65.8,34.0,75.1]
print(marks)
print(type(marks))
print(len(marks))
print(marks[1])
print(marks[4])

#different type of the list we can print in python and mutable process

Details=["Laddu",86.06,3,"Ballia"]
Details[0]="Fradeen"
print("Details is:")
print("Nmae:",Details[0])
print("pecentage",Details[1])
print("Rank:",Details[2])
print("distric:",Details[3])

#sublisting of the list

marks=[30,69,78,90,14,65]
print(marks[1:5])
print(marks[-6:-3])


#List  (append,sort,sort+reverse,revers,insert,remove ,pop)

list=[1,2,3,6,5,4,7]
list.append(8)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.insert(8,9)
print(list)
list.remove(6)
print(list)
list.pop(3)
print(list)

#TUPLES in python (tuples is immutable)
#we only STORE THE ELEMENTS in tuple we use()intead of []

tpl=(23,45,67,90)
print(tpl,type(tpl))
print(tpl[0:])
print(len(tpl))

#[1]wap to ask the user to enter names of their 3 favorite movies & store them in a list 

movies=[]
movies.append(input("enter the first movie:"))
movies.append(input("enter the second movie:"))
movies.append(input("enter the third movie:"))
print(movies)

#second mathod to solve above program
movie=[]
mov1=input("entyer the 1 movie:")
movie.append(mov1)
mov2=input("entyer the second movie:")
movie.append(mov2)
mov3=input("enter the third movie:")
movie.append(mov3)
print(movie)




#wap to check if a list contains a palindrome of element (Hint: use copy()methode)


list=[1,2,3,2,1]
copylist=list.copy()
copylist.reverse()
if(copylist==list):
    print("palindrone")
else:
    print("not palindrone")   

 
#wap to count the number of student with "a" grade in the following tuple .
        #("c,"d","a","a","b","b","a")

  #STORE THE ABOVE VALUES IN THE LIST &SORT THEM FROM "a"TO "d"    
   
grade=("c","d","a","a","b","b","a")
print(grade.count("a"))
print(grade.count("d"))
list=["c","d","a","a","b","b","a"]
list.sort()
print(list)