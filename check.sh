#!/bin/sh
export NUMBAPRO_NVVM="/usr/local/cuda-9.2/nvvm/lib64/libnvvm.so"
#export NUMBAPRO_CUDALIB="/usr/local/cuda-9.2/targets/x86_64-linux/lib/"
export NUMBAPRO_CUDALIB="/usr/local/cuda-9.2/lib64/"
export NUMBAPRO_LIBDEVICE="/usr/local/cuda-9.2/nvvm/libdevice/"

python3 check.py

