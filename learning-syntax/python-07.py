#Lists
thislist=["apple","banana","cherry","cherry",False]
print(thislist)
print(len(thislist))
print(type(thislist))

#list Constructor
thislist2=list(("apple","banana","cherry"))
print(thislist2)

#Acessing List Elements
print(thislist[0])

#Negative Indexing
print(thislist[-1])
print(thislist[-2])

#range of indexes
print(thislist[1:3])
print(thislist[-3:-1])

thislist3=["apple","banana","cherry"]
if "apple" in thislist3:
    print("Yes, 'apple' is present in the list")
    
thislist3[1]="mangoa"
print(thislist3)

thislist3[1:3]=["mango","orange"]
print(thislist3)
    
thislist3[1:3]=["WaterMelon"]
print(thislist3)

thislist3.insert(1,"Potato")
print(thislist3)

thislist3.insert(2,"Lemon")
print(thislist3)    


#Append: to add item at the end of the list
thislist4=[]
thislist4.append("potato")

#Extend :to append elements from another list to the current list
thislist4.extend(thislist)
print(thislist4)
thislist4.extend(["Kiwi","Orange"])
print(thislist4)


#Remove Specified Item 
#it will remove the specified the first specified item
thislist5=[]
thislist5.append("apple")
thislist5.append("banana")
thislist5.append("cherry")
print(thislist5)
thislist5.remove("banana")
print(thislist5)

#Remove Specified Index
#it will remove the item at the specified index
thislist5.pop(1)
print(thislist5)
thislist5.clear()
#del thislist5[1]
del thislist5


#loop through

thislist6=["adasd","asdas","sdfsd"]
for i in thislist6:
    print(i)
for x in range(len(thislist)):
    print(thislist[x])
    
    
    
 #List comprehension
 #List comprehension is a compact way to create lists
 #it is a one liner code to create a list
thislist8=[x for x in thislist if x != "banana"]
print(thislist8)

thislist10=["apple","orange","potato","lemon"]
thislist11=[x if x!="banana" else "orange" for x in thislist10 ]
print(thislist11)


#Sort List
#sort() method sorts the list in-place
#it means that it changes the original list
thislist12=["banana","orange","apple","potato"]
thislist12.sort()
thislist12.reverse()
thislist12.sort(reverse=True)

#Copy
thislist13=thislist12.copy()
thislist13.sort()
thislist14=thislist13[:]


#Join List
thislist15=thislist13+thislist14


"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""












