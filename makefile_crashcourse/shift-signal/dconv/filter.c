#include <stdio.h>

#include "filter.h"
enum { SUPPORT = _N_ } ;

void filter_create(const float delta, float out[SUPPORT])

{
	fprintf(stderr, "hello filter create %f\n", delta);
}
