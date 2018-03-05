import urllib2
import os
import zipfile
import shutil
from subprocess import call
from sys import executable as e


gimp_be_download = "https://github.com/J216/gimp_be/archive/master.zip"

dependancies = ["runtime", "wget", "numpy", "TwitterAPI"]

py_exec = executable.replace('pythonw','python')
py_path = e[:e.rfind("\\")+1].replace("\\","/")
py_lib = py_path+"\\Lib"

os.chdir(py_path)

pip_install = py_exec + " -m pip install "
wget_download = py_exec + " -m wget "

# install dependancies
call(pip_install+" ".join(dependancies))

# download from github
call(wget_download+gimp_be_download)
# unzip gimp_be-master.zip
if os.path.isfile("./gimp_be-master.zip"):
    zip = zipfile.ZipFile("gimp_be-"+gimp_be_download[gimp_be_download.rfind('/')+1:])
    zip.extractall()
    del(zip)

# delete zip file
os.remove("./gimp_be-master.zip")
if os.path.isdir("./gimp_be-master/gimp_be"):
    # copy settings
    os.rename("./Lib/site-packages/gimp_be/settings/settings.ini", "./settings.ini")
    # remove older version
    shutil.rmtree("./Lib/site-packages/gimp_be", ignore_errors=False, onerror=None)
    # copy new version
    os.rename("./gimp_be-master/gimp_be", "./Lib/site-packages/gimp_be")
    # restore settings.json
    os.rename("./settings.ini","./Lib/site-packages/gimp_be/settings/settings.ini")
    # update update script
    os .remove("./Scripts/gimp_be_update.py")
    os.rename("./gimp_be-master/install/gimp_be_update_windows.py", "./Scripts/gimp_be_update.py")
    # clean up
    shutil.rmtree("./gimp_be-master", ignore_errors=False, onerror=None)
