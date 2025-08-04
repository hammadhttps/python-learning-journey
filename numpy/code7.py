import numpy as np

#sorting arrays

np1=np.array([1,2,3,4,5,2])
np2=np.array([[1,2,4],[1,-1,0],[2,1,0]])
print(np.sort(np1))
print(np.sort(np2))



#searching

x=np.where(np1==3)
print(x)
#searching in 2d array
x=np.where(np2==1)
print(x)


#filtering
np4=np.array([1,2,4,32,4,3,2,2])
np5=np.array([1,2,4,32,4,3,2,2])
x=[True,False,True,False,True,False,True,False]

print(np4[x])
filter=[]
for x in np4:
    if x%2==0:
        filter.append(x)
        
        
        
filter1=np1%2==0
print(filter1)