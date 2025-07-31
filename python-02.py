#Gloabl variables

x="Hello world"

def myFunc():
    z="world"
    global y
    y="hello"
    x="World"
    print(x)


#printing Z gives error
#print(z)
myFunc()
print(y)
