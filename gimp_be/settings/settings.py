import datetime
import os
import urllib2
from ConfigParser import ConfigParser
import inspect

path_settings=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

configfile_name = path_settings+"/settings.ini"
config = ConfigParser()
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
config.read(configfile_name)
settings_data=config._sections


def saveSettings():
    global settings_data
    # Check if there is already a configurtion file
    if not os.path.isfile(configfile_name):
        # Create the configuration file as it doesn't exist yet
        cfgfile = open(configfile_name, 'w')
        config._sections=settings_data
        Config.write(cfgfile)
        cfgfile.close()

def loadDefaultSettings():
    global settings_data
    os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
    config.read("default_"+configfile_name)
    settings_data=config._sections

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

