#Dictionaries
#Key-value Pair
#Unordered collection of key-value pairs
#Key is unique and immutable
#Value can be any data type
#Dictionaries are mutable
#Dictionaries are denoted by curly brackets {} or by using the dict() function

thisdict={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)
print(thisdict["brand"])
print(thisdict.keys())
property(thisdict.get("model"))
print(thisdict.values())
print(thisdict.items())
thisdict["color"]="blue"
thisdict.update({"brand":"Lemozeen"})
print(thisdict)
thisdict.pop("model")
print(thisdict)


thisdict2=dict(thisdict)
print(thisdict2)


#Nested Dictionaries
#A dictionary can contain another dictionary as its value
#Nested dictionaries are useful when you want to store data in a more structured way

myfamily={
    "child1":{
        "name":"John",
        "age":10
        },
    "child2":{
        "name":"Jane",
        "age":12
        }
}

print(myfamily["child1"]["name"])


"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""
