#!/usr/bin/env python3

print("""
#include <stdio.h>

#include "dconv.h"
void dconv(const float * in, const float * w, float * out)
{
	fprintf(stderr, "hello synthetic dconv\\n");
}
""")
