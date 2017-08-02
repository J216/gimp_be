import os
import json
from time import sleep
from subprocess import Popen, PIPE
exiftool_location="c:/scr/Tools/exiftool.exe"
from gimp_be import settings_data
from datetime import datetime

def getEXIFTags(file_name):
    from subprocess import Popen, PIPE
    sleep(1)
    p = Popen([exiftool_location, '-j',file_name], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"")
    tags=json.loads(output)[0]
    del(p)
    sleep(2)
    return tags

def setEXIFTag(file_name, tag='Comment', info='8888888-8888888-8888888-888888888888'):
    from subprocess import call
    sleep(1)
    cmd=exiftool_location+' -' + tag +'="'+ info.replace('"','')+'" "'+file_name+'"'
    result=(call(cmd)==0,cmd)
    sleep(2)
    os.remove(file_name+'_original')
    return result

def setEXIFTags(file_name, tags={"XPComment":"Test complete1!","Comment":"Test Complete2"}):
    from subprocess import call
    sleep(1)
    tag_string=""
    for key in tags.keys():
        tag_string=tag_string+' -' + key +'="'+ str(tags[key]).replace('"','')+'"'
    cmd=exiftool_location+tag_string+' "'+file_name+'"'
    print cmd
    result=(call(cmd)==0,cmd)
    sleep(2)
    os.remove(file_name+'_original')
    return result

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
    sleep(2)
    try:
        os.remove(fn+'_original')
    except:
        print "file already deleted"