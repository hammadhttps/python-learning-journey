#Sets  

# A set is a collection which is unordered,unchangeable and unindexed
# Sets are used to store unique values
# Sets are mutable
# Sets are used to store unique values
# Sets are unordered,unchangeable and unindexed

set1={"apple","banana","cherry"}
print(set1) 

set2={"apple",4.2,1,False}
print(set2)

set2.add(2)
set2.update(set1)
print(set2)


set1.remove("apple")
set1.discard("apple") #doesnt give error

print(set1.pop())
set1.clear()


#Join sets
"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

sett1={"a","b","c","d"}
sett2={1,2,4,6,8}
print(sett1.union(sett2))


sett3=sett1|sett2
sett3.update(set1)

sett3.intersection(sett2) #set4=set1 & set2
sett1.difference(set1)


sett1.symmetric_difference(sett2)


"""
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns True if all items of this set is present in another set
 	<	Returns True if all items of this set is present in another, larger set
issuperset()	>=	Returns True if all items of another set is present in this set
 	>	Returns True if all items of another, smaller set is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
"""