# pwd
# mkdir packages
# cd packages
# wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2021.05-Linux-x86_64.sh

# bash Anaconda3-2021.05-Linux-x86_64.sh

# conda create -n SoCo python=3.7
# conda activate SoCo

pip install torch==1.6.0 torchvision==0.7.0

# accimage
pip install --prefix=/opt/intel/ipp ipp-devel
pip install git+https://github.com/pytorch/accimage

# apex
git clone https://github.com/NVIDIA/apex 
cd apex/
# P100, P40, V100 and 2080Ti
ENV TORCH_CUDA_ARCH_LIST="6.0;6.1;7.0;7.5"
pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./

# detectron2
python -m pip install 'git+https://github.com/hologerry/detectron2.git' --upgrade --force-reinstall

# Install MMCV and MMdetection
pip uninstall pycocotools
pip install mmcv-full==1.2.4 -f https://download.openmmlab.com/mmcv/dist/cu102/torch1.6.0/index.html --upgrade --force-reinstall

# git clone https://github.com/hologerry/mmdetection.git
# cd mmdetection
# pip install -r requirements/build.txt --upgrade --force-reinstall
# pip install -v -e . --upgrade --force-reinstall


pip install scikit-image



# mkdir datasets
# cd datasets
# mkdir imagenet
# cd imagenet
# hdfs dfs -get hdfs://haruna/home/byte_arnold_lq_vc/user/zhanglibin.buaa/datasets/imagenet-object-localization-challenge.zip
# unzip imagenet-object-localization-challenge.zip
# tar -xvf imagenet_object_localization_patched2019.tar.gz