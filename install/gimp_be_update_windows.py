import os
from time import sleep
import zipfile
import shutil
from subprocess import call
from sys import executable as e

errors = []

py_exec = e.replace('pythonw','python')
py_path = e[:e.rfind("\\")+1].replace("\\","/")
gimp_be_path = py_path+"\\Lib\\site-packages\\gimp_be"
gimp_be_installed = os.path.isdir(gimp_be_path)

gimp_be_download = "https://github.com/J216/gimp_be/archive/master.zip"
get_pip_download = "https://bootstrap.pypa.io/get-pip.py"

dependancies = ["runtime", "wget", "numpy", "TwitterAPI"]

pip_install = py_exec + " -m pip install "
wget_download = py_exec + " -m wget "

os.chdir(py_path)

#install pip
if not gimp_be_installed:
    try:
        import pip
    except:
        import urllib
        urllib.urlretrieve (get_pip_download, "get-pip.py")
        # install dependancies
        errors.append("pip not previously installed, install: "+str(call(py_exec + " get-pip.py")))

# install dependancies
errors.append("install dependancies: "+str(call(pip_install+" ".join(dependancies))))

# download from github
errors.append("download gimp_be: "+str(call(wget_download+gimp_be_download)))

# unzip gimp_be-master.zip
try:
    if os.path.isfile("./gimp_be-master.zip"):
        zip = zipfile.ZipFile("gimp_be-"+gimp_be_download[gimp_be_download.rfind('/')+1:])
        zip.extractall()
        del(zip)
        #clean up
        sleep(.1)
        os.remove("./gimp_be-master.zip")
except:
    errors.append("download and unzip and delete zip: Error")

if os.path.isdir("./gimp_be-master/gimp_be"):
    # copy settings
    if gimp_be_installed:
        os.rename("./Lib/site-packages/gimp_be/settings/settings.ini", "./settings.ini")
        # remove older version
        try:
            shutil.rmtree("./Lib/site-packages/gimp_be", ignore_errors=False, onerror=None)
        except:
            errors.append("gimp_be module folder couldn't be deleted")
            sleep(1)
    # copy new version
    os.rename("./gimp_be-master/gimp_be", "./Lib/site-packages/gimp_be")
    if gimp_be_installed:
        # restore settings.ini
        os.rename("./settings.ini","./Lib/site-packages/gimp_be/settings/settings.ini")
    # update update script
    try:
        os .remove("./Scripts/gimp_be_update.py")
    except:
        errors.append("Old copy of gimp_be update script not found or couldn't be deleted")
    os.rename("./gimp_be-master/install/gimp_be_update_windows.py", "./Scripts/gimp_be_update.py")
    try:
        # clean up
        shutil.rmtree("./gimp_be-master", ignore_errors=False, onerror=None)
    except:
        errors.append("couldn't delete temp files")


if len(e) == 0:
    print("completed with no error")
else:
    for e in errors:
        print(e)
