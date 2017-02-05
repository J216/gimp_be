    import datetime, os, json, urllib2

def loadSettings():
    # type: () -> object
    """

    :rtype: bool
    """
    global settings_data
    settings_file=os.path.join(os.path.abspath(__file__)[0:os.path.abspath(__file__).replace('\\','/').rfind('/')], 'settings.json')
    if os.path.isfile():
        with open(settings_file) as json_data_file:
            settings_data = json.load(json_data_file)
    else:
        settings_data = {"not_loaded": "1"}
    return settings_data


def saveSettings():
    global settings_data
    settings_file=os.path.join(os.path.abspath(__file__)[0:os.path.abspath(__file__).replace('\\','/').rfind('/')], 'settings.json')
    try:
        with open(settings_file, 'w') as fp:
            json.dump(settings_data, fp)
        return True
    except:
        return False


def loadDefaultSettings():
    global settings_data
    default_settings_file=os.path.join(os.path.abspath(__file__)[0:os.path.abspath(__file__).replace('\\','/').rfind('/')],'default_settings.json')
    try:
        with open(default_settings_file) as json_data_file:
            settings_data = json.load(json_data_file)
        return True
    except:
        return False


def getLocationData():
    loc_data = ()
    try:
        dict = ''
        dict = urllib2.urlopen('http://www.geoplugin.net/json.gp').read()
        city = dict[dict.find('"', dict.find('city') + 6) + 1:dict.find('"', dict.find('city') + 7)]
        state = dict[dict.find('"', dict.find('gion') + 6) + 1:dict.find('"', dict.find('gion') + 7)]
        latitude = dict[dict.find('"', dict.find('latitude') + len('latitude')) + 3:dict.find('"', dict.find(
            'latitude') + len('latitude') + 3)]
        longitude = dict[dict.find('"', dict.find('longitude') + len('longitude')) + 3:dict.find('"', dict.find(
            'longitude') + len('longitude') + 3)]
        weather_url = 'http://forecast.weather.gov/MapClick.php?lat=' + str(latitude) + '&lon=' + str(
            longitude) + '&FcstType=json'
        location_data = urllib2.urlopen(weather_url).read()
        location_data[
        location_data.find('"Temp":"', location_data.find('currentobservation')) + len('"Temp":"'):location_data.find(
            '"', location_data.find('"Temp":"', location_data.find('currentobservation')) + len('"Temp":"'))]
        current_temp = location_data[location_data.find('"Temp":"', location_data.find('currentobservation')) + len(
            '"Temp":"'):location_data.find('"', location_data.find('"Temp":"',
                                                                   location_data.find('currentobservation')) + len(
            '"Temp":"'))]
        current_weather = location_data[
                          location_data.find('"Weather":"', location_data.find('currentobservation')) + len(
                              '"Weather":"'):location_data.find('"', location_data.find('"Weather":"',
                                                                                        location_data.find(
                                                                                            'currentobservation')) + len(
                              '"Weather":"'))]
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


def initialSettings():
    