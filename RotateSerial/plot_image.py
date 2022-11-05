import basic_rotate as b
import numpy as np
import math as m
import matplotlib.pyplot as plt
from PIL import Image

plt.rcParams['agg.path.chunksize'] = 1000000



def main():
	# Get 2-dimentional array of image.
	# img = Image.open("Roberts-Claude-Shannon-1.jpg").convert('L')
	img = Image.open("uva.jpg").convert('L')
	imgArray = np.array(img)
	length = imgArray.shape[0] * imgArray.shape[1]
	n_x = imgArray.shape[0]
	n_y = imgArray.shape[1]

	# Reshape to 1-D
	imgArray = imgArray.reshape((length))

	dst_array_scatter = b.rotateScatter(imgArray,m.pi/180,n_x,n_y)
	dst_array_gather = b.rotateGather(imgArray,m.pi/180,n_x,n_y)

	figure, axis = plt.subplots(2, 2)

	#original image
	axis[0, 0].imshow(np.reshape(np.array(imgArray, dtype=np.float32), (n_x,n_y)))
	axis[0, 0].set_title("Original_image")

	# Final image
	axis[0, 1].imshow(np.reshape(np.array(dst_array_gather, dtype=np.float32), (n_x,n_y)))
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