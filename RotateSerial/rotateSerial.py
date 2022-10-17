from cmath import cos,sin
from hmac import new
from math import floor, pi
import math
from operator import index
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np




# As of 17 Oct, matplotlib does not work on 3.10 or above.

n = 100
# image = np.array([0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0])
image = np.array([0]*200)
image = np.concatenate((image,np.array([1]*n)))
image = np.concatenate((image,np.array([0]*9700)))
plt.xlim([0, n])
plt.ylim([0, n])


# image.shape  = (-1,n)
# print(image)

# plt.imshow(image, cmap="gray")
# plt.show()

angle = math.pi/4;
cosine_of_angle = cos(angle)
sin_of_angle = sin(angle)
def rotate(A):
    newA = np.array([0]*len(A))
    for i in range(0,len(A)):
        x = int(i % n)
        y = int(i / n)
        
        new_x = cosine_of_angle * x - sin_of_angle * y
        new_y = sin_of_angle * x + cosine_of_angle * y
        new_x = new_x.real
        new_y = new_y.real
        
        new_x = round(new_x)
        new_y = round(new_y)
        
        if new_x < n and new_x >= 0 and new_y >= 0 and new_y < n:
            idx = new_y * n + new_x
            newA[idx] = A[i]
            
    return newA
        
rotatedimage = rotate(image)
rotatedimage.shape = (-1,n)

plt.imshow(rotatedimage,cmap="gray")
plt.show()

