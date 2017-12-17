import datetime
import os
import json
import urllib2
from gimp_be import settings_data, settings_file

def loadSettings():
    global settings_data
    global settings_file
    if settings_file == '':
        settings_file=os.path.abspath(__file__)
        if ".pyc" in settings_file:
            settings_file=settings_file.replace('.pyc','.json')
        if ".py" in settings_file:
            settings_file=settings_file.replace('.py','.json')
    if os.path.isfile(settings_file):
        with open(settings_file) as json_data_file:
            settings_data = json.load(json_data_file)
        return (True, settings_data)
    else:
        return (False, {"not_loaded": "1"})

def saveSettings():
    global settings_data
    global settings_file
    with open(settings_file, 'w') as json_data_file:
        json.dump(settings_data,json_data_file)
        return (True, settings_data)
    print 'Save settings failed.'
    return (False, {"not_saved": "1"})

def loadDefaultSettings():
    global settings_data
    default_settings_file=os.path.abspath(__file__)[0:-11] + 'default_settings.json'
    if os.path.isfile(settings_file):
        with open(default_settings_file) as json_data_file:
            settings_data = json.load(json_data_file)
        return (True, settings_data)
    else:
        return (False,{"not_loaded": "1"})

def getLocationData():
    loc_data = ()
    dict = ''
    try:
        dict = urllib2.urlopen('http://www.geoplugin.net/json.gp').read()
        city = dict[dict.find('"', dict.find('city') + 6) + 1:dict.find('"', dict.find('city') + 7)]
        state = dict[dict.find('"', dict.find('gion') + 6) + 1:dict.find('"', dict.find('gion') + 7)]
        latitude = dict[dict.find('"', dict.find('latitude') + len('latitude')) + 3:dict.find('"', dict.find('latitude') + len('latitude') + 3)]
        longitude = dict[dict.find('"', dict.find('longitude') + len('longitude')) + 3:dict.find('"', dict.find('longitude') + len('longitude') + 3)]
        weather_url = 'http://forecast.weather.gov/MapClick.php?lat=' + str(latitude) + '&lon=' + str(longitude) + '&FcstType=json'
        location_data = urllib2.urlopen(weather_url).read()
        location_data[
        location_data.find('"Temp":"', location_data.find('currentobservation')) + len('"Temp":"'):location_data.find('"', location_data.find('"Temp":"', location_data.find('currentobservation')) + len('"Temp":"'))]
        current_temp = location_data[location_data.find('"Temp":"', location_data.find('currentobservation')) + len('"Temp":"'):location_data.find('"', location_data.find('"Temp":"', location_data.find('currentobservation')) + len('"Temp":"'))]
        current_weather = location_data[location_data.find('"Weather":"', location_data.find('currentobservation')) + len('"Weather":"'):location_data.find('"', location_data.find('"Weather":"', location_data.find('currentobservation')) + len('"Weather":"'))]
        loc_data = (city, state, latitude, longitude, current_temp, current_weather)
    except:
        loc_data = ('0', '0', '0', '0', '0', '0')
    return loc_data

def updateLocationData(save=1, print_conditions=1):
    now = datetime.datetime.now()
    global settings_data
    temp_loc=getLocationData()
    if not temp_loc[0] == '0':
        settings_data["location"]["city"]=temp_loc[0]
        settings_data["location"]["state"] = temp_loc[1]
        settings_data["location"]["latitude"] = temp_loc[2]
        settings_data["location"]["longitude"] = temp_loc[3]
        settings_data["location"]["tempf"] = temp_loc[4]
        settings_data["location"]["weather"] = temp_loc[5]
        if save == 1:
            saveSettings()
        if print_conditions == 1:
            print now.strftime("%A %B %d - %I:%M%p")
            print settings_data["location"]["city"] + ' ' + settings_data["location"]["state"]
            print settings_data["location"]["tempf"] + ' ' + settings_data["location"]["weather"]
            print settings_data["user"]["author"] + ' on ' + settings_data["network"]["host_name"] + '\n'
        return True
    else:
        return False

def calcW(height=1080, aspect=[16,9]):
    return (height/aspect[1])*aspect[0]

def calcH(width=1920, aspect=[16,9]):
     return (width/aspect[0])*aspect[1]

def setImageSize(dim=[512,512]):
    global settings_data
    settings_data['image']['width'] = str(dim[0])
    settings_data['image']['height'] =  str(dim[1])
    settings_data['image']['x_center'] = str(dim[0]/2)
    settings_data['image']['y_center'] = str(dim[1]/2)
    saveSettings()

def setImageTitle(new_title=""):
    global settings_data
    if not new_title == "":
        settings_data['image']['title']=new_title
    saveSettings()

def setExportFileType(ef="png"):
    global settings_data
    settings_data['image']['export_file_type']=ef
    saveSettings()

def setExportName(en=""):
    global settings_data
    if not en == "":
        settings_data['path']['export_name']=en
        saveSettings()

def setDefaultSavePath(ds=""):
    global settings_data
    if not ds == "":
        settings_data['path']['default_save_path']=ds
        saveSettings()

def setArtFolder(af=""):
    global settings_data
    if not af == "":
        settings_data['path']['art_folder']=ds
        saveSettings()

def setAuthor(name='GIMP Artist'):
    global settings_data
    settings_data['user']['author'] = name
    saveSettings()

def setDeveloperMode(mode="False"):
    global settings_data
    settings_data['development']['dev_mode']=unicode(str(mode=="True"), "utf-8")
    saveSettings()

