#universals functions in numpy

import numpy as np

np1=np.array([1,2,34,5,10])
np2=np.array([1,2,3,4,5])
np3=np.array([-1,-2,-3,-4,-4,-1])

print(np1+np2)  #addition of two arrays


#functions
print(np.mean(np1))
print(np.sqrt(np2))
print(np.absolute(np3))

#exponents
print(np.exp(np1))

#min-max
print(np.min(np1))
print(np.max(np1))

#log
print(np.log(np3))


