import numpy as np

#shaping numpy arrays

np1=np.array([1,2,3,45,7,45,4,3,3,3,3,3,3,2,4,12])
np2=np.array([[1,2,3,4,5,6,7,8],[2,23,213,2,32,13,12,99],[2,23,213,2,32,13,12,99]])
print(np1)

print(np1.shape)

##prints rows and cols
print(np2.shape)

# reshaping

# 1 rows and sixteen cols
np2=np2.reshape(1,24)
print(np2)
print(np2.shape)

# 3d shaping
np3=np2.reshape(1,8,3)
print(np3)

#flatten a array
np4=np2.flatten()
np5=np1.reshape(-1)
print(np5)
print(np4)

