#include <iostream>
#include <cuda.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

__global__ void rotateScatter(float *A, float *dst_array, const float angle,
							  const int width, const int height)
{
	float c_x = width / 2.0;
	float c_y = height / 2.0;

	// Iterating horizontally through the image.
	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{

			// Subtract center coordinates, so that we rotate with respect to the
			// center of the image.
			float x = j - c_x;
			float y = i - c_y;

			// Rotation operation
			float dst_x = cos(angle) * x - sin(angle) * y;
			float dst_y = sin(angle) * x + cos(angle) * y;

			// Add back the center "vector"
			dst_x = (int)(dst_x + c_x);
			dst_y = (int)(dst_y + c_y);

			// Check if the resulting point is inside the boundary of the image, i.e
			// 0->max_x, 0->max_y.
			if (dst_x >= 0 && dst_x < width && dst_y >= 0 && dst_y < height)
			{
				// If so then assign value from original array to dst_array at idx
				// location.
				int idx = dst_y * width + dst_x;
				dst_array[idx] = A[i * width + j];
			}
		}
	}
}

int main()
{
	const char *pathname = "../Images/rectangle.raw";
	int width = 300;
	int height = 200;

	const int n = width * height;
	float *A = (float *)malloc(sizeof(float) * n);
	float *R = (float *)malloc(sizeof(float) * n);
	float *d_a, *d_out;

	// Open input image and populate input array A.
	FILE *raw_p = fopen(pathname, "rb");
	if (raw_p)
	{
		fread(A, sizeof(float), n, raw_p);
	}

	// Modify input array A by normalizing values from 0->1.
	for (int i = 0; i < n; ++i)
	{
		A[i] = A[i] / 255.0;
	}

	// Allocate memory on device.
	cudaMalloc((void **)&d_a, sizeof(float) * n);
	cudaMalloc((void **)&d_out, sizeof(float) * n);

	// Copy Image array to device.
	cudaMemcpy(d_a, A, sizeof(float) * n, cudaMemcpyHostToDevice);

	// Call Kernel rotateScatter
	rotateScatter<<<1, 1>>>(d_a, d_out, M_PI / 4, width, height);

	cudaMemcpy(R, d_out, sizeof(float) * n, cudaMemcpyDeviceToHost);

	// Open output file and write result array.
	FILE *fp = fopen("test_image.raw", "wb");
	if (fp)
	{
		size_t r = fwrite(R, sizeof(R[0]), n, fp);
		printf("wrote %zu elements out of %d requested\n", r, n);
	}

	cudaFree(d_a);
	cudaFree(d_out);
	fclose(fp);
	fclose(raw_p);
	free(A);
	free(R);

	return 0;
}