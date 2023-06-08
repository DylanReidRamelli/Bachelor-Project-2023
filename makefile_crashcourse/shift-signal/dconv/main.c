#include <stdio.h>
#include <stdlib.h>

#include "filter.h"
#include "dconv.h"

void dconv(const float *, const float *, float *);

int main 
(
		const int argc,
		const char * argv[] 
	 )
{	
	if (2 != argc)
	{
		fprintf(stderr,
				"usage: %s <shift-value>\n",
				argv[0]);

			return EXIT_FAILURE;
	}

	enum { FILTER_SUPPORT = _N_ };

	float w[FILTER_SUPPORT];

	filter_create(atof(argv[1]), w);

	float input[100];
	fread(input, sizeof(input), 1, stdin);

	float output[100];
	dconv(input, w, output);

	fwrite(output, sizeof(output), 1, stdout);

	return EXIT_SUCCESS;
}
