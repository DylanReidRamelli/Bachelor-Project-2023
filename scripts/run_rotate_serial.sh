#! /bin/bash


_build_all(){
	cmake ..
	make -j4 
	./rotate_noloss
	cd ../scripts/python/
	python3.10 image_io.py ../../build/test_image_noloss.raw ../../build/image_info.raw
	# for (( i=1; i<=16; i++ ))
	# do
	# 	angle = 360/16 * i
	#   	python3.10 image_io.py ../../build/test_image_noloss.raw ../../build/image_info.raw ${angle}
	# done
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


