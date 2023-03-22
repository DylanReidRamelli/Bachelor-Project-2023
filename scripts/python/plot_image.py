import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

A = 1.0
B = 1.0
C = 0.5
n = 50

# Define image dimensions
width = 1000
height = 1000

def alpha_0(r):
    return 2 * np.pi * np.sin(C * r)

# Define function to be plotted
def g(alpha, r):
    return A * np.exp(-(r * alpha - alpha_0(r)) / r) * np.cos(B * r**(3/2)) * r

def generate_graph():
	r = np.linspace(1,360,num=360, dtype=int)
	alpha = np.radians(np.linspace(1,360,num=360, dtype=int))
	z = np.zeros_like(alpha)
	for i in range(n):
	    z += g(alpha, r * (i+1))
	plt.plot(alpha,z)
	plt.savefig("../../Images/graph_sinusoid.png")



def generate_image():

	# Generate image data
	x, y = np.meshgrid(np.linspace(-1, 1, width), np.linspace(-1, 1, height))
	r = np.sqrt(x**2 + y**2)
	theta = np.angle(x + y*1j)
	z = np.zeros_like(r)

	for i in range(n):
	    z += g(theta, r * (i + 1))

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