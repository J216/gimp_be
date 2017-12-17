## Linux updater for gimp_be for linux, test on debian

#change workind directory to home folder 
cd $HOME

#download and unzip gimp_be
rm master.zip
wget https://github.com/J216/gimp_be/archive/master.zip
unzip master.zip
cd gimp_be-master

#copy gimp_be pack to python lib folder
sudo rm -r /usr/lib/gimp/2.0/python/gimp_be/
sudo cp -r ./gimp_be/ /usr/lib/gimp/2.0/python/

#delete install files
cd ..
rm -r ./gimp_be-master/
