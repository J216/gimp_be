cd $HOME
mkdir gimp_be
cd gimp_be
wget https://github.com/J216/gimp_be/archive/master.zip
sudo cp ./gimp_be/ /usr/lib/gimp/2.0/python/gimp_be/
wget https://bootstrap.pypa.io/get-pip.py
sudo /usr/bin/python2.7 ./get-pip.py
sudo /usr/bin/python2.7 -m pip install TwitterAPI
cd ..
rm -r ./gimp_be/
