def myfunc(fname,lname):
    print(fname+lname)
    
def myfunc2(**params):
    print(params["lname"])
    
myfunc("Hammad ","Hassan")   
myfunc2(fname="Hammad",lname="Hassan")


#Recursion
def tru_recursion(k):
    if k >0:
        result=k+tru_recursion(k-1)
        print(result)
    else:
      result=0
      return result      


print("Recursion Example Results:")
tru_recursion(6)        



#lambda
#use it when anonymus functions are required for a short period of time
x=lambda a:a+10
print(x(5))

y=lambda a,b:a*b
print(y(5,6))

z=lambda a,b,c:a+b+c
print(z(1,2,3))

