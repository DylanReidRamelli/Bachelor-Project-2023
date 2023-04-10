import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import math

# Define image dimensions
width = 256
height = 256

A = 1.0
B = 1.0
C = 0.5
n = 5


def alpha_0(r):
    return (2*np.pi * np.sin(C * r))

# Define function to be plotted
def g(alpha, r):
    return A * np.exp(-np.mod(alpha - alpha_0(r), 2*np.pi)**2 / r) * np.cos(B * r**(3/2))
    # return A * np.exp(-(r * np.mod(alpha - alpha_0(r), 2*np.pi) - alpha_0(r)) / r) * np.cos(B * r**(3/2)) * r


# plot 1-d 
# search 
def generate_graph():


	r = np.linspace(1,n,num=n, dtype=int)
	alpha = np.radians(np.linspace(1,360,num=360, dtype=int))

	plt.title("Plot of circle with radius up to: " + str(n))
	plt.xlabel("Angle in radians.")
	plt.ylabel("g(alpha,radius)")


	for j in range(1,n + 1):
		z = np.zeros_like(alpha)
		for i in range(0,len(alpha)):
			z[i]= g(alpha[i], j)
		plt.plot(alpha,z)

	plt.savefig("../../Images/graph_sinusoid.png")



def generate_image():

	# Generate image data
	x, y = np.meshgrid(np.linspace(-np.pi, np.pi, width), np.linspace(-np.pi, np.pi, height))
	r = np.sqrt(x**2 + y**2)
	theta = np.angle(x + y*1j)
	# theta = np.arctan2(y, x)

	# print(theta)
	z = np.zeros_like(r)

	# n_size = math.floor(len(r)/ (n + 1))
	# print(n_size)
	# print(r)

	for i in range(1, n+1):
		z += g(theta, r * i)


	# z += g(theta, 1)

	# for i in range(0, len(r)):
	# 	for j in range(0,len(r)):
	# 		if r[i][j] == 1:
	# 			z += g(theta, 1)


	# # Normalize and convert to grayscale
	z = (z - np.min(z)) / (np.max(z) - np.min(z))
	z = (255 * z).astype(np.uint8)

	# print(z)

	# # Create image and save to file
	img = Image.fromarray(z, mode='L')
	img.save('../../Images/wrapped_sinusoid.png')

def main():
	generate_graph()
	generate_image()



if __name__ == '__main__':
	main()