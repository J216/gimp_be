# study variables
import datetime
active_study = {
    "study_creation_date": str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')),
    "study_name": "digital paintings",
    "study_folder": "./studies",
    "current_study_folder": "0",
    "study_description": "GIMP digital image study",
    "study_tweet_hashtags": "#GIMP #digitalart #python",
    "study_tweet": " ",
    "session_loaded": "0",
    "session_name": "Rainy Tuesday Evening",
    "study_session_iteration": "0"
}


def saveStudySettings():
    import json
    global active_study
    global settings_data
    try:
        with open('study.json', 'w') as fp:
            json.dump(settings_data, fp)
        return True
    except:
        return False


def studyStart(name='', description='', folder=''):
    # set file name and folder
    # make new folder
    # serialize name set
    # set tweet for study
    # set image comments
    # study has subfolders for sessions
    # create method to fill tweet to capacity with hashtags
    # study ==> sessions --> iterations --> image,filename,title,date,comment
    global active_study
    global settings_data
    ## ALL OF THESE SHOULD BE IN THE JSON FOR ACTIVE_STUDY ##
    # global study_session_iteration
    # global study_description
    # global study_name
    # global study_session_iteration_name
    # global study_creation_date
    # global study_tweet
    # global current_study_folder  # whole folder name? or just the name in the studies folder?
    # global studies_folder
    # global session_loaded
    import os
    import datetime
    time_stamp = datetime.datetime.now()
    from gimp_be.utils.string_tools import imageTitle

    os.chdir(studies_folder)
    active_study['study_session_iteration'] = '0'
    active_study['session_loaded'] = '1'

    # if os.path.isfile('my_settings.dat'):
    # TODO determine folder naming convention
    # TODO determine twitter shortener method
    # ASK user if they want to load study if it already exists.
    # if os.path.exists('/this/is/a/dir') print 'Study already exists, please loadStudy('study name')' and escape

    # handles folder NOT DONE
    if folder == '0':
        print('auto generate study name')
    else:
        study_name = name
    # current_study_folder=

    # TODO create folder if study does not exist

    # handles name of study
    if name == '0':
        active_study['study_name'] = imageTitle(2) + ' ' + datetime.datetime.now()[:10]
    else:
        active_study['study_name'] = name
    # handles tweet composition
    if study_tweet == 'default tweet':
        active_study['study_tweet'] = 'Study in digital painting. ' + active_study['study_name'] + ' ' + active_study['study_session_iteration']
    else:
        active_study['study_tweet'] = tweet
    # handles description
    if study_description == '0':
        active_study['study_description'] = 'Study in digital painting.'
    else:
        active_study['study_description'] = description
    # set session name
        active_study['study_session_iteration_name'] = studySessionName()
    # sets creation date
        active_study['study_creation_date'] = datetime.datetime.now()[:10]
    # write study file ./study.xml


# does collage of multiple images from study
def studyComposite():
    print('does collage of multiple images from study')


# session name generator
def studySessionName():
    global weather
    import random
    week = ['Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday']
    return weather.replace('/', ' ') + ' ' + random.choice(('Red', 'Blue', 'Black', 'Yellow', 'Green')) + ' ' + week[
        datetime.datetime.today().weekday()]


# start session
def studySessionStart(name='',session_it=u'0'):
    global active_study
    if name == '':
        name= studySessionName()
    active_study['session_name'] = name
    active_study['study_session_iteration'] = session_it

        # setup session variables


# does collage of multiple images from study
def studySessionComposite():
    print('does collage of multiple images from study')


# exports current image as jpg with study naming convention
def studyIterationSave():
    global active_study
    study_session_iteration = str(int(active_study['study_session_iteration']) + 1)
    print('Save current state')


# exports current iteration and tweets it with study tweet and iteration number
def studyIterationTweet():
    print('tweet current state')

