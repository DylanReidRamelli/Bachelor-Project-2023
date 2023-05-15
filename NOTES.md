# General Notes
- Rotate corners before allocating array. / DONE
- Rotate 360 times by 1 degrees. / DONE
- Rotate a couple of rows by 360 degrees. Compare the values and check for error margin. / DONE

# Bilinear Interpolation
- Scan pixels of transformed image and find the corresponding pixel in original image.
- Compute the transformed pixel's value from the bilinear interpolation of the four neighboring 
pixels of the original image.

# Bicubic interpolation
- Same thing as before but with more neighbours and using a third degree interpolant.

# Article procedure
- What the article does is rotate the fourier transform of the image and the fourier transform of the kernel used. Then use convolution between the two and bicubic interpolation. 
