from cmath import cos,sin
from hmac import new
from math import floor, modf, pi
import math
from operator import index, mod
from xml.etree.ElementTree import tostring
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np  
from PIL import Image, ImageOps


# As of 17 Oct, matplotlib does not work on 3.10 or above.



def draw_rectangle(image, width, height):
    for y in range(0,height):
        for x in range(0,width):
            x_geometry = 1.0*x/width
            y_geometry = 1.0*y/height
            value = x_geometry > 0.25 and x_geometry < 0.75 and y_geometry > 0.25 and y_geometry < 0.75
            image[y*width + x] = value
            
            
def rotateScatter(A,angle):
    cosine_of_angle = cos(angle)
    sin_of_angle = sin(angle)
    newA = np.array([0]*len(A),np.uint8)
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

def rotateGather(A,angle):
    cosine_of_angle = cos(angle)
    sin_of_angle = sin(angle)
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

n = 50
dims_tuple =(2000, 1303)
angle = math.pi/180
# image = np.array([0]*2500)
# draw_rectangle(image,50,50)

# Import grayscale image.
image = Image.open('Roberts-Claude-Shannon-1.jpg')

# Save original image.
image.save("original_image.png")

#Transform image into numpy array.
image = np.asarray(image)
#Some info about the array
print("Some information regarding the numpy array of the image:",
      "\nType:" ,image.dtype, "\nShape:",image.shape, "\nStrides:",image.strides)

# print(image)

modfied_image_array = np.zeros((image.shape[0], image.shape[1]))
for i in range(0,image.shape[0]):
    for j in range(0,image.shape[1]):
        modfied_image_array[i][j] = image[i][j][0]
# image = np.reshape(image,dims_tuple)
# print(modfied_image_array)
modfied_image_array = modfied_image_array.flatten()
print(modfied_image_array)


        
rotatedimage = rotateScatter(modfied_image_array,angle)

# print(rotatedimage)


# # print(rotatedimage)
rotatedimage.shape = dims_tuple

print(rotatedimage)

pilimage = Image.fromarray(rotatedimage)
pilimage.save("scatterRotate_image.png")

# print(rotatedimage)

# plt.imshow(rotatedimage,cmap="gray")
# plt.savefig("scatterRotate_image.png")


# inverseimage = rotateGather(image,angle)

# inverseimage.shape = (-1,n)
# plt.imshow(inverseimage,cmap="gray")
# plt.savefig("gatherRotate.png")


# max_frames = 90
# angle_animation = pi/180
# # Create n images of scatter and gather for ffmpeg video
# for i in range(0,max_frames):
    
#     rotatedimage = rotateScatter(image,angle_animation)
    
#     rotatedimage.shape = dims_tuple
    
#     plt.imshow(rotatedimage,cmap="gray")
#     plt.savefig("scatter/scatterRotate_image"+ str(i) + ".png")


#     # inverseimage = rotateGather(image,angle_animation)

#     # inverseimage.shape = (-1,n)
#     # plt.imshow(inverseimage,cmap="gray")
#     # plt.savefig("gather/gatherRotate_image" + str(i) + ".png")
#     angle_animation+=pi/180


