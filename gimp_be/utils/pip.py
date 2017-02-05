import subprocess, os, urllib, sys
#install pip --windows only, I think--
def installPIP():
    import os, urllib,subprocess
    gimp_python=sys.executable[:-5]+'.exe'
    os.chdir(gimp_python[:-10])
    urllib.urlretrieve ("https://bootstrap.pypa.io/get-pip.py", "get-pip.py")
    return subprocess.call("python get-pip.py")


#install module using PIP install, provide module name as string
def pipInstall(module):
    import os, urllib, subprocess
    gimp_python=sys.executable[:-5]+'.exe'
    os.chdir(gimp_python[:-10])
    print "python -m pip install "+module
    return subprocess.call("python -m pip install "+module)

