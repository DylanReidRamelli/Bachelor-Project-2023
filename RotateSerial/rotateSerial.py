from cmath import cos,sin
from hmac import new
from math import floor, pi
import math
from operator import index
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np




# As of 17 Oct, matplotlib does not work on 3.10 or above.

def draw_rectangle(image, width, height):
    for y in range(0,height):
        for x in range(0,width):
            x_geometry = 1.0*x/width
            y_geometry = 1.0*y/height
            value = x_geometry > 0.25 and x_geometry < 0.75 and y_geometry > 0.25 and y_geometry < 0.75
            image[y*width + x] = value

n = 100
# image = np.array([0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0])
image = np.array([0]*10000)
draw_rectangle(image,100,100)
            
plt.xlim([0, n])
plt.ylim([0, n])

# fig = plt.figure(figsize=(3, 1))


# image.shape  = (-1,n)
# print(image)

# fig.add_subplot(n,n)
# plt.imshow(image, cmap="gray")
# plt.show()


angle = math.pi/4;
cosine_of_angle = cos(angle)
sin_of_angle = sin(angle)
def rotateScatter(A):
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

def rotateGather(A):
    newA = np.array([0]*len(A))
    for i in range(0,len(newA)):
        x = int(i % n)
        y = int(i / n)
        
        new_x = cosine_of_angle * x + sin_of_angle * y
        new_y = -sin_of_angle * x + cosine_of_angle * y
        new_x = new_x.real
        new_y = new_y.real
        
        new_x = round(new_x)
        new_y = round(new_y)
        
        if new_x < n and new_x >= 0 and new_y >= 0 and new_y < n:
            idx = new_y * n + new_x
            newA[i] = A[idx]
            
    return newA
    
        
# rotatedimage = rotateScatter(image)
# rotatedimage.shape = (-1,n)

# fig.add_subplot(n,n)

inverseimage = rotateGather(image)


inverseimage.shape = (-1,n)
plt.imshow(inverseimage,cmap="gray")
plt.show()
