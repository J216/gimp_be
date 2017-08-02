settings_data = {'location':{'city':''}}
settings_file=''

def loadSettings():
    global settings_data
    global settings_file
    if settings_file == '':
        settings_file=os.path.abspath(__file__)[0:-11] + 'settings.json'
    if os.path.isfile(settings_file):
        with open(settings_file) as json_data_file:
            settings_data = json.load(json_data_file)
        return (True, settings_data)
    else:
        return (False, {"not_loaded": "1"})


from settings import *
settings_data = loadSettings()[1]

from core import *
from network import *
from image import *
from utils import *
from draw import *
from paint import *

