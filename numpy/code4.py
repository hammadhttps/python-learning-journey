#copy vs view

"""view is also a copy of array 
but it is also connected to the array"""


import numpy as np


np1=np.array([1,2,3,4,5,6])
np2=np1.view()
np3=np1.copy()


print(f'original np1 {np1}')
print(f'original np2 {np2}')

np1[0]=10
print(f'np2 {np2}')
print(f'np3 {np3}')