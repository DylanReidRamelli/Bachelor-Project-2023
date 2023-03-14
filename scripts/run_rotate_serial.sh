#! /bin/bash


_build_all(){
	cmake ..
	make -j4 
	# ./rotate_noloss
	# cd ../scripts/python//
	# python3.10 image_io.py ../../build/test_image_noloss.raw ../../build/image_info.raw
	rm info/image_info*
	rm images/test_image_noloss_*
	for (( i=0; i<=360; i++ ))
	do
		./rotate_noloss ${i} info/image_info_${i}.raw images/test_image_noloss_${i}.raw 
	done


	cd ../scripts/python
	rm output_images/.png*
	for (( i=1; i<=360; i++ ))
	do
		python3.10 image_io.py ../../build/images/test_image_noloss_${i}.raw ../../build/info/image_info_${i}.raw ${i}
	done

	cd output_images
	rm out.mp4
	# ffmpeg -framerate 2 -pattern_type glob -i '*.png' -c:v libx264 -pix_fmt yuv420p out.mp4
	ffmpeg -start_number 0 -i image_%d.png -r 24 output.mp4
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


