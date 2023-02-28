#include "basic_rotate.hpp"
#include <fstream>
#include <iostream>
#include <vector>

void read_png_file(const std::vector<float> &output, const int width,
                   const int height, const std::string &file_path) {

  std::string line;
  std::ifstream mFile(file_path);
  if (mFile.is_open()) {

    while (!mFile.eof()) {
      std::cout << " open";
      std::getline(mFile, line);
      std::cout << line << std::endl;
    }
  }
}

int main(int argc, const char *argv[]) {

  // const std::string file_path = "../../images/rectangle.png";
  // std::vector<float> A;
  // int width = 300;
  // int height = 200;

  // read_png_file(A, width, height, file_path);
}