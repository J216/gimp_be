from gimp_be.settings.settings import *
from gimp_be.utils.string_tools import *


def tweetImage(message,image_file):
    """
    Tweet image with message
    :param message:
    :param image_file:
    :return:
    """
    from TwitterAPI import TwitterAPI
    global settings_data
    CONSUMER_KEY = settings_data['twitter']['CONSUMER_KEY']
    CONSUMER_SECRET = settings_data['twitter']['CONSUMER_SECRET']
    ACCESS_TOKEN_KEY = settings_data['twitter']['ACCESS_TOKEN_KEY']
    ACCESS_TOKEN_SECRET = settings_data['twitter']['ACCESS_TOKEN_SECRET']
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    file = open(image_file, 'rb')
    data = file.read()
    r = api.request('statuses/update_with_media', {'status':message}, {'media[]':data})
    return str(str(r.status_code))


def tweetText(opt=0):
    """
    return string of twitter message
    :param opt:
    :return:
    """
    global settings_data
    import datetime
    now = datetime.datetime.now()
    
    updateLocationData()
    title = imageTitle(2)
    city = settings_data["location"]["city"]
    state = settings_data["location"]["state"]
    host_name = settings_data["network"]["host_name"]
    tempf = settings_data["location"]["tempf"]
    weather = settings_data["location"]["weather"]
    hashtags = settings_data["twitter"]["hashtags"]
    time_stamp = str(datetime.datetime.now())
    tweet_text = ''
    if opt == 0:
        tweet_text = title + '\nby ' + settings_data['user']['author'] + '\n' + city + ' ' + state + ' | ' + host_name + '\n' + tempf + 'F ' + weather + '\n' + now.strftime("%A %B %d - %I:%M%p")
    elif opt == 1:
        tweet_text = title + '\nby ' + settings_data['user']['author'] + ' ' + time_stamp[:4] + '\n' + hashtags
    else:
        tweet_text = title + '\nby ' + settings_data['user']['author'] + ' ' + time_stamp[:4]
    return tweet_text


def tweetHashtags(hashtags=('0', '1', '2')):
    """
    hashtag string
    :param hashtags:
    :return:
    """
    tag_string = ''
    for tag in hashtags:
        tag_string = tag_string + '#' + tag + ' '
    return tag_string.strip()
