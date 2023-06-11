_build_all() {
    # for ((i = 0; i <= 100; i = i + 0.1)); do
    #     python3 direct_convolution_2.py ${i} images/image_info_${i}.png
    # done
    time=125959
    echo "${time:0:2}":"${time:2:2}":"${time:4:2}"
    # shopt -s extglob
    for i in $(seq 0.0 .1 10.0); do
        t="${i//./}"
        j="${t:0:2}"
        k="${t:2:3}"
        # echo ${t:2:3}

        if [ "${k}" != "" ]; then
            echo ${j}${k}
            # python3 direct_convolution_2.py ${i} images/image_info_${j}_${k}.png
        else
            # echo "Banana"
            # echo ${j}
            python3 direct_convolution_2.py ${i} images/image_info_${j}_0.png
        fi

        # python3 direct_convolution_2.py ${i} images/image_info_${integer_part}_${fractional_part}.png
    done

    for i in $(seq 0.0 .1 10.0); do
        t="${i//./}"
        j="${t:0:2}"
        k="${t:2:3}"

        if [ "${k}" != "" ]; then
            # echo ${j}${k}
            python3 direct_convolution_2.py ${i} images/image_info_${j}_${k}.png

        fi

    done

}

if [[ -d images ]]; then
    cd images
    rm -rf *
    cd ..
    _build_all
fi

if [[ ! -d images ]]; then
    mkdir images
    _build_all
fi
