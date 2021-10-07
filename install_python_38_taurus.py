#!/bin/bash
#
# This script installs a python 3.8 kernel. 
# It is written for the Taurus cluster at TU Dresden.
#
# Author: Robert Haase, robert.haase@tu-dresden.de
#         DFG Cluster of Excellence "Physics of Life"
#
module load Anaconda3
mkdir p38-kernel_20211007
conda create -y --prefix /home/$USER/p38-kernel_20211007/p38-kernel python=3.8 #Changed: v3.8
conda init bash #Added: Need to init conda (i.e. put it into our ".bashrc")
source $HOME/.bashrc #Added: load the stuff that was just appended to ".bashrc"
conda activate /home/$USER/p38-kernel_20211007/p38-kernel
conda install -y ipykernel
pip install pyclesperanto_prototype
pip install stardist
pip install cellpose
pip install pyclesperanto_assistant stackview
pip install tensorflow-gpu
python -m ipykernel install --user --name p38-kernel --display-name="P38"

