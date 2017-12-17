## Linux installer for gimp_be for linux, test on debian

#change workind directory to home folder 
cd $HOME

#install needed packages
sudo apt update
supo apt install gimp
sudo apt install unzip
sudo apt install exiftool

#download and unzip gimp_be
wget https://github.com/J216/gimp_be/archive/master.zip
unzip master.zip
cd gimp_be-master

#copy gimp_be pack to python lib folder
sudo mkdir /usr/lib/gimp/2.0/python/gimp_be/
sudo cp -r ./gimp_be/ /usr/lib/gimp/2.0/python/

#install python dependancies
wget https://bootstrap.pypa.io/get-pip.py
sudo /usr/bin/python2.7 ./get-pip.py
sudo /usr/bin/python2.7 -m pip install TwitterAPI

#delete install files
cd ..
rm -r ./gimp_be-master/
