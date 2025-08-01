class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
     return f"{(self.name)}({self.age})"  
 
    def myfunc(self):
        print("Hello my name is "+self.name) 
        
p1=Person("john",36)
print(p1.name)
print(p1.age)
print(p1)
p1.myfunc()


#Inheritance
class Parent:
    def __init__(object,fname,lname):
        object.fname=fname
        object.lname=lname
    def printfunc(object):
        print(object.fname+" "+object.lname)
   
   
class Child(Parent):
    def __init__(self,fname,lname,age,sex):
        super().__init__(fname,lname)
        self.age=age
        self.sex=sex
        
    def printfunc(self):
        super().printfunc()
        print(self.age)
        print(self.sex)
        
    def greet(self):
        print("Hello my name is "+self.fname+" "+self.lname)
        
        
        
p1=Child("hammad","Hassan",23,"Male")
p1.greet()     

#Python Iterators
#An iterator is an object that contains a countable number of values
 

class Numbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.end:
            result = self.start
            self.start += 1
            return result
        else:
            raise StopIteration 
        

mynumbers=Numbers(1,10)
myiter=iter(mynumbers)
while True:
    try:
      print(next(myiter))
    except StopIteration:
        print("Iteration is over")
        break
    
    
    
    
#Polymorphism
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()
  
  
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
    
    
    
    
x = 300
def myfunc():
  x = 200
myfunc()
print(x)



        