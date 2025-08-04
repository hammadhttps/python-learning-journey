import numpy as np


np1=np.array([1,2,3,4,5,6])
np2=np.array([7,8,9,10,11,12])

#slicing
print(np1[1:5])

print(np1[3:])

print(np1[-3:-1])

#slicing with steps
print(np1[1:5:2])
print(np1[::2])


#slicing 2d Array

np3=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np3[1,2])
print(np3[1:3,1:3])