#! /bin/bash


_build_all(){
	cmake ..
	make -j4 
	./rotate_noloss
	cd ../scripts/python/
	python3.10 image_io.py ../../build/test_image_noloss.raw ../../build/image_info.raw
}

if [[ -d build ]]
then
	cd build
	_build_all
fi

if [[ ! -d build ]]
then
	mkdir build
	cd build
	_build_all
fi


