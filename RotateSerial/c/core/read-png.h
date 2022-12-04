#include <png.h>
#include <stdlib.h>

#include "posix-util.h"

void rpng(const char *pathname, int *const xc, int *const yc,
          unsigned char **const out) {
  FILE *fp = NULL;
  POSIX_CHECK(fp = fopen(pathname, "rb"));

  png_structp png =
      png_create_read_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);
  if (!png)
    abort();

  png_infop info = png_create_info_struct(png);
  if (!info)
    abort();

  if (setjmp(png_jmpbuf(png)))
    abort();

  png_init_io(png, fp);

  png_read_info(png, info);

  int width = *xc = png_get_image_width(png, info);
  int height = *yc = png_get_image_height(png, info);

  fprintf(stderr, "loading <%s> of %d x %d pixels\n", pathname, *xc, *yc);
  png_byte color_type = png_get_color_type(png, info);
  png_byte bit_depth = png_get_bit_depth(png, info);

  // Read any color_type into 8bit depth, RGBA format.
  // See http://www.libpng.org/pub/png/libpng-manual.txt

  if (bit_depth == 16)
    png_set_strip_16(png);

  if (color_type == PNG_COLOR_TYPE_PALETTE)
    png_set_palette_to_rgb(png);

  // PNG_COLOR_TYPE_GRAY_ALPHA is always 8 or 16bit depth.
  if (color_type == PNG_COLOR_TYPE_GRAY && bit_depth < 8)
    png_set_expand_gray_1_2_4_to_8(png);

  if (png_get_valid(png, info, PNG_INFO_tRNS))
    png_set_tRNS_to_alpha(png);

  if (color_type == PNG_COLOR_TYPE_RGB)
    fprintf(stderr, "color is rgb\n");

  // These color_type don't have an alpha channel then fill it with 0xff.
  if (color_type == PNG_COLOR_TYPE_RGB || color_type == PNG_COLOR_TYPE_GRAY ||
      color_type == PNG_COLOR_TYPE_PALETTE)
    png_set_filler(png, 0xFF, PNG_FILLER_AFTER);

  if (color_type == PNG_COLOR_TYPE_GRAY ||
      color_type == PNG_COLOR_TYPE_GRAY_ALPHA)
    png_set_gray_to_rgb(png);

  png_read_update_info(png, info);

  png_bytep *row_pointers = NULL;
  if (row_pointers)
    abort();

  row_pointers = (png_bytep *)malloc(sizeof(png_bytep) * height);
  for (int y = 0; y < height; y++) {
    row_pointers[y] = (png_byte *)malloc(png_get_rowbytes(png, info));
  }

  png_read_image(png, row_pointers);

  const ptrdiff_t rc = height, pc = width;

  unsigned char *data = (unsigned char *)malloc(4 * rc * pc);

  /* RGB to RGBA conversion by default now */
  for (int r = 0; r < rc; ++r) {
    unsigned char *out = data + 4 * pc * r;
    unsigned char *in = row_pointers[rc - 1 - r];

    for (int p = 0; p < pc; ++p) {
      out[0 + 4 * p] = in[0 + 4 * p];
      out[1 + 4 * p] = in[1 + 4 * p];
      out[2 + 4 * p] = in[2 + 4 * p];
      out[3 + 4 * p] = in[3 + 4 * p];
    }
  }

  /* cleanup png */

  for (int r = 0; r < rc; ++r)
    free(row_pointers[r]);

  free(row_pointers);

  *out = data;

  POSIX_CHECK(0 == fclose(fp));

  png_destroy_read_struct(&png, &info, NULL);
}