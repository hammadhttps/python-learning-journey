#Tuples
"""
A tuple is a collection of items that can be of any data type, including strings, integers,
floats, and other tuples.
It is unchangable and it is ordered
"""

tupl1=("apple","banana","cherry")
print(len(tupl1))
print(len(tupl1))
tuple2=("apple",1,"banna","cherry")
print(tuple2)
tuple3=tuple(("apple","apple2","apple3"))
print(tuple3)
print(tuple2[1])
print(tuple2[2])

#other built in functions are same as list
#append,extend,insert,remove,sort,reverse,index,insert,etc. but they

tuple4=("apple","banana","cherry")
y=list(tuple4)
y[1]="kiwi"
tuple4=tuple(y)
print(tuple4)


y=("orange",)
tuple4+=y
print(y)

#Unpack tuples 
tuple5=("apple","banana","cherry")
(apple,yellow,furit)=tuple5
print(apple)

tuple6=tuple5*2
print(tuple6)

tuple6.count("apple")
print(tuple6.count("apple"))
print(tuple6.index("banana"))


"""
Tuple Methods:
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""