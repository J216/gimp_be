import os
import json
from time import sleep
from subprocess import Popen, PIPE
from gimp_be import settings_data
from datetime import datetime
from sys import platform

if "win" in platform:
    exiftool_location="exiftool.exe"
elif "linux" in platform:
    exiftool_location="exiftool"
else:
    exiftool_location="exiftool.exe"


def getEXIFTags(file_name):
    p = Popen([exiftool_location, '-j',file_name], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    try:
        output, err = p.communicate(b"")
        tags=json.loads(output)[0]
        p.terminate()
    except:
        tags="failed to load"
    return tags

def setEXIFTag(file_name, tag='Comment', info='8888888-8888888-8888888-888888888888'):
    cmd=exiftool_location+' -' + tag +'="'+ info.replace('"','')+'" "'+file_name+'"'
    p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    try:
        output, err = p.communicate(b"")
        result=(err,output,cmd)
        p.terminate()
    except:
        result=""
    if os.path.isfile(file_name+'_original'):
        os.remove(file_name+'_original')
    return result

def setEXIFTags(file_name, tags={"XPComment":"Test complete1!","Comment":"Test Complete2"}):
    from subprocess import call
    tag_string=""
    for key in tags.keys():
        tag_string=tag_string+' -' + key +'="'+ str(tags[key]).replace('"','')+'"'
    cmd=exiftool_location+tag_string+' "'+file_name+'"'
    p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    try:
        output, err = p.communicate(b"")
        result=(err,output,cmd)
        p.terminate()
    except:
        result=""
    if os.path.isfile(file_name+'_original'):
        os.remove(file_name+'_original')
    return result

def increaseRating(file_name):
    t=getEXIFTags(file_name)
    if "Rating" in t.keys():
        if not str(t['Rating'])=="5":
            r=str(int(t['Rating'])+1)
            return setEXIFTag(file_name,"Rating",r)
    else:
        return setEXIFTag(file_name,"Rating","5")

def decreaseRating(file_name):
    t=getEXIFTags(file_name)
    if "Rating" in t.keys():
        if not str(t['Rating'])=="0":
            r=str(int(t['Rating'])-1)
            return setEXIFTag(file_name,"Rating",r)
    else:
        return setEXIFTag(file_name,"Rating","0")

def qXDT(fn,comment=""):
    global settings_data
    setEXIFTags(fn,{"Copyright":settings_data['user']['author']+" "+datetime.now().strftime('%Y'),
                    "License":settings_data['image']['license'],
                    "Comment":comment,
                    "XPComment":comment,
                    "Description":comment,
                    "ImageDescription":comment,
                    "SEMInfo":comment,
                    "Artist":settings_data['user']['author'],
                    "Author":settings_data['user']['author'],
                    "Software":"GIMP 2.8 Python 2.7 EXIFTool",
                    "Title":comment[:comment.find('\n')],
                    "XPTitle":comment[:comment.find('\n')],
                    "Make":"GIMP",
                    "Model":"Python",
                    "Rating":"5"})
    sleep(1)
    if os.path.isfile(fn+'_original'):
        os.remove(fn+'_original')