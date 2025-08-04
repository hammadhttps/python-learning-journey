import numpy as np

#iterating through numpy arrays

np1=np.array([1,2,3,4,5,23,323,23,23,1,3])
np2=np.array([[1,2,3,4,5,23,323,23],[1,2,3,4,5,23,2,32]])


# for x in np1:
#     print(x)
    
#2d array    
for x in np2:
    for y in x:
        print(y)
        
        
np3=np.array([[[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]],[[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]]])       
#3d array
print(np3)
for x in np3:
    for y in x:
        for z in y:
            print(z)
            
            
 #nd iter
for x in np.nditer(np3):
    print(x)
 