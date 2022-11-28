#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#ifndef _WIN32
#define fseeko64 fseek
#define ftello64 ftell
#endif
#ifndef NDEBUG
#define POSIX_CHECK(stmt)								\
	do													\
	{													\
		if (!(stmt))									\
		{												\
			fprintf(stderr,								\
					"error: %s\n", strerror(errno));	\
														\
			fprintf(stderr,								\
					"during: "							\
					#stmt);								\
														\
			fprintf(stderr, "\n"						\
					" in file* %s at line %d\n"			\
					"\nexiting now.\n",					\
					__FILE__, __LINE__);				\
														\
			fflush(stderr);								\
														\
			exit(EXIT_FAILURE);							\
		}												\
	}													\
	while(0)
#else
#define POSIX_CHECK(stmt)								\
	do													\
	{													\
		if (!(stmt))									\
		{												\
			fprintf(stderr,								\
					"error: %s\n", strerror(errno));	\
														\
			exit(EXIT_FAILURE);							\
		}												\
	}													\
	while(0)
#endif

static inline
size_t count_slices_posix (
	FILE * f,
	size_t nbytes_slice)
{
	size_t old = ftello64(f);
	POSIX_CHECK(0 == fseeko64(f, 0, SEEK_END));

	size_t fsize = ftello64(f);
	POSIX_CHECK(0 == fseeko64(f, old, SEEK_SET));

	return fsize / nbytes_slice;

static inline
size_t count_slices_pathname_posix (
	const char * pathname,
	size_t nbytes_slice)
{
	FILE * f;

	POSIX_CHECK(f = fopen(pathname, "rb"));

	const size_t retval = count_slices_posix (f, nbytes_slice);

	POSIX_CHECK(0 == fclose(f));
	return retval;
}

#include <sys/time.h>
static inline double rdtss()
{
	struct timeval tv;
	POSIX_CHECK(0 == gettimeofday(&tv, NULL));

	return tv.tv_sec + 1e-6 * tv.tv_usec;
}