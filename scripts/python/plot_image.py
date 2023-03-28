import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Define image dimensions
width = 512
height = 512

A = 1.0
B = 1.0
C = 0.5
n = 2


def alpha_0(r):
    return (2*np.pi * np.sin(C * r))

# Define function to be plotted
def g(alpha, r):
    return A * np.exp(-np.mod(alpha - alpha_0(r), 2*np.pi)**2 / r) * np.cos(B * r**(3/2))
    # return A * np.exp(-(r * np.mod(alpha - alpha_0(r), 2*np.pi) - alpha_0(r)) / r) * np.cos(B * r**(3/2)) * r


# plot 1-d 
# search 
def generate_graph():

	n_radius = 2

	r = np.linspace(1,n_radius,num=n_radius, dtype=int)
	alpha = np.radians(np.linspace(1,360,num=360, dtype=int))

	print(alpha)

	plt.xlabel("Angle in radians.")
	plt.ylabel("g(alpha,radius)")


	for j in range(1,n_radius):
		z = np.zeros_like(alpha)
		for i in range(0,len(alpha)):
			z[i]= g(alpha[i], j)
		plt.plot(alpha,z)

	plt.savefig("../../Images/graph_sinusoid.png")



def generate_image():

	# Generate image data
	x, y = np.meshgrid(np.linspace(-np.pi, np.pi, width), np.linspace(-np.pi, np.pi, height))
	r = np.sqrt(x**2 + y**2)
	# theta = np.angle(x + y*1j)
	theta = np.arctan2(y, x)

	# print(theta)
	z = np.zeros_like(r)

	for i in range(1,n):
	    z += g(theta, r * i )

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