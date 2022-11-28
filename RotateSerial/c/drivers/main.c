#include "../core/basic_rotate.h"
#include "../core/read-png.h"
#include <assert.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char *argv[]) {
  const char *pathname = "../../images/rectangle.png";
  unsigned char **out;
  rpng(pathname, 300, 200, out);
  return 0;
}