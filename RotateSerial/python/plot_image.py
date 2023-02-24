import math as m
import basic_rotate as b
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

plt.rcParams['agg.path.chunksize'] = 1000000

# Print out info about images. Input and output. 
# Create image in gimp, super basic image. Primitive shapes.


def main():
	# Get 2-dimentional array of image.
	# img = Image.open("../images/Roberts-Claude-Shannon-1.jpg").convert('L')
	img = Image.open("../images/rectangle.png").convert('L')
	# img = Image.open("../images/square.png").convert('L')
	# img = Image.open("uva.jpg").convert('L')
	imgArray = np.array(img)

	alpha = m.pi/6
	# take out a color rotate it, then do the same for each channel.
	length = imgArray.shape[0] * imgArray.shape[1]
	n_x = imgArray.shape[0]
	n_y = imgArray.shape[1]

	print(n_x,n_y)


	# Reshape to 1-D
	imgArray = imgArray.reshape((length))
	dtype=imgArray.dtype

	# pdb.set_trace()
	dst_array_scatter = b.rotateScatter(imgArray,alpha,n_x,n_y,0)
	dst_array_gather = b.rotateGather(imgArray,alpha,n_x,n_y,0)
	dst_array_gather_noloss, sizeX, sizeY = b.rotateGatherNoLoss(imgArray,alpha,n_x,n_y,0)

	figure, axis = plt.subplots(2, 2)

	#original image
	axis[0, 0].imshow(np.reshape(np.array(imgArray, dtype=dtype), (n_x,n_y)))
	axis[0, 0].set_title("Original_image")

	# Final image
	axis[0, 1].imshow(np.reshape(np.array(dst_array_gather_noloss, dtype=dtype), (sizeX,sizeY)))
	axis[0, 1].set_title("Resulting image (gather rotate)")

	axis[1, 1].plot(imgArray, dst_array_scatter)
	axis[1, 1].set_title("Scatter rotate (unrolled signal)")
	# axis[0,0].xlabel("index") 
	# axis[0,0].ylabel("value") 
	# plt.ylabel("value") 
	  
	axis[1, 0].plot(imgArray, dst_array_gather)
	axis[1, 0].set_title("Gather rotate (unrolled signal)")
	# axis[0,1].xlabel("index") 
	# axis[0,1].ylabel("value")


	# Display

	plt.show()


if __name__ == '__main__':
	main()