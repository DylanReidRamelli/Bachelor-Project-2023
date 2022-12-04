#include "../core/basic_rotate.h"
#include "../core/read-png.h"
#include <assert.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char *argv[]) {
  char *pathname = "../../images/rectangle.png";
  unsigned char *out = "../../images/modified_rectangle.png";

  rpng(pathname, 300, 200, out);

  // printf("%s", out);

  return 0;
}