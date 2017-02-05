import os
import subprocess
import sys
import urllib


#install pip --windows only, I think--
def installPIP():
    urllib.urlretrieve ("https://bootstrap.pypa.io/get-pip.py", "get-pip.py")
    return subprocess.call(os.path.join(sys.executable, "get-pip.py"))


#install module using PIP install, provide module name as string
def pipInstall(module, print_out=1):
    gimp_python = os.path.join(sys.executable, " -m pip install ", module)
    if print_out == 1:
        print gimp_python
    return subprocess.call(gimp_python)
