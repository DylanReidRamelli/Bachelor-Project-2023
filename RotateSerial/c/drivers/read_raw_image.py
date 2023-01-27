#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import image as mpimg
from PIL import Image
import io

# with open(image_info_path,"r") as f:
# 	lines = f.readlines()
#     nx = lines[0]
#     ny = lines[1]


def main(image_path):
    nx = 300
    ny = 200
    n = nx * ny

    file = open(image_path, 'rb')
    image_data = file.read()
    img = Image.frombytes("L", (300,200), image_data)

    plt.title("Original Image")
    plt.xlabel("X pixel scaling.")
    plt.ylabel("Y pixel scaling.")

    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    main(sys.argv[1])
