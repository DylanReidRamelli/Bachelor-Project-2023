#! /bin/bash

_build_all(){
	cmake .. -DBACHELOR_ENABLE_CUDA=ON
	make -j

	rm info/image_info*
	rm images/test_image_noloss_*
	for (( i=0; i<=360; i++ ))
	do
		./rotate_noloss_CUDA ${i} info/image_info_${i}.raw images/test_image_noloss_${i}.raw 
	done


	cd ../scripts/python/output_images
	rm *.png
	cd ..
	for (( i=1; i<=360; i++ ))
	do
		python3 image_io.py ../../build_cuda/images/test_image_noloss_${i}.raw ../../build_cuda/info/image_info_${i}.raw ${i}
	done
	cd output_images
	rm output.mp4
	ffmpeg -i image_%d.png -c:v h264 -crf 20 -pix_fmt yuv420p output.mp4

}

if [[ -d build_cuda ]]
then
	cd build_cuda
	_build_all
fi

if [[ ! -d build_cuda ]]
then
	mkdir build_cuda
	cd build_cuda
	_build_all
fi