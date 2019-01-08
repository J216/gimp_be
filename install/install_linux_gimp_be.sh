#!/bin/bash


## Linux installer for gimp_be for linux, test on debian

#install needed packages
sudo apt update
sudo apt install gimp unzip exiftool python-pip python3-pip -y

#copy gimp_be pack to python lib folder
sudo mkdir /usr/lib/gimp/2.0/python/gimp_be/
sudo cp -r ../gimp_be/ /usr/lib/gimp/2.0/python/

#install python dependancies
sudo /usr/bin/python2.7 -m pip install TwitterAPI numpy

