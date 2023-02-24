#include <iostream>
#include <cuda.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

__global__ void rotateScatter(const float A[], float dst_array[], const float angle,
							  const int width, const int height)
{
}

int main()
{
	const char *pathname = "../Images/rectangle.raw";
	int width = 300;
	int height = 200;

	const int n = width * height;
	float A[n];
	float result[n];

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

	// Call Kernel rotateScatter

	// Open output file and write result array.
	FILE *fp = fopen("test_image.raw", "wb");
	if (fp)
	{
		size_t r = fwrite(result, sizeof(result[0]), n, fp);
		printf("wrote %zu elements out of %d requested\n", r, n);
	}

	fclose(fp);
	fclose(raw_p);

	return 0;
}