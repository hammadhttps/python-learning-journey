import numpy as np


np1=np.array([0,1,2,3,4,5,6,7,8,9,10])
print(np1)

##length
print(np1.shape)

np2=np.arange(10)
print(np2)


##steps
np3=np.arange(0,10,2)
print(np3)



## multi-D array

np4=np.zeros((2,10))
print(np4)


np5=np.full((10),6)
print(np5)


np6=np.full((2,10),6)
print(np6)


##converting list into nparrays


my_list=[1,2,3,4,5]
np8=np.array(my_list)
print(np8)