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
n = 10


def alpha_0(r):
    return (2 * np.pi * np.sin(C * r)) - np.pi

# Define function to be plotted
def g(alpha, r):
    return A * np.exp(-((alpha - alpha_0(r))**2) / r) * np.cos(B * (r**(3/2)))

def generate_graph():
	r = np.linspace(1,360,num=360, dtype=int)
	alpha = np.radians(np.linspace(1,360,num=360, dtype=int))
	z = np.zeros_like(alpha)
	for i in range(n):
	    z += g(alpha, r * (i+1))

	plt.xlabel("Angle in radians.")
	plt.ylabel("g(alpha,radius)")
	plt.plot(alpha,z)
	plt.savefig("../../Images/graph_sinusoid.png")



def generate_image():

	# Generate image data
	x, y = np.meshgrid(np.linspace(-np.pi, np.pi, width), np.linspace(-np.pi, np.pi, height))
	r = np.sqrt(x**2 + y**2)
	theta = np.angle(x + y*1j)
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