from cmath import cos,sin
from math import floor, pi
from operator import index
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np




# As of 17 Oct, matplotlib does not work on 3.10 or above.


image = np.array([0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0])

image.shape  = (-1,5)
print(image)

plt.imshow(image, cmap="gray")
plt.show()

angle = pi/2;
cosine_of_angle = cos(angle)
sin_of_angle = sin(angle)
def rotate(A):
    newA = np.array([0]*25)
    for i in range(0,len(A)):
        x = int(i % 5)
        y = int(i / 5)
        new_x = cosine_of_angle * x - sin_of_angle * y
        new_y = sin_of_angle * x - cosine_of_angle * y
        new_x = new_x.real
        new_y = new_y.real
        
        new_x = round(new_x)
        new_y = round(new_y)
        
        if new_x < 5 and new_x > 0 and new_y > 0 and new_y < 5:
            if A[i] == 1:
                idx = new_y * 5 + new_x
                print("Prev index: ", i, "New Index: ", idx, "\n")
                newA[idx] = A[i]
            
    return newA
        
rotatedimage = rotate(image)
rotatedimage.shape = (-1,5)

print(rotatedimage)
plt.imshow(rotatedimage,cmap="gray")
plt.show()
