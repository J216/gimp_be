try:
    import TwitterAPI
except:
    pipInstall("TwitterAPI")


def setTwitterAPIKeys(ACCESS_TOKEN_KEY="NOT_SET",CONSUMER_KEY="NOT_SET",CONSUMER_SECRET="NOT_SET",ACCESS_TOKEN_SECRET="NOT_SET"):
    global settings_data
    if not ACCESS_TOKEN_KEY == "NOT_SET":
        settings_data['twitter']['ACCESS_TOKEN_KEY']=ACCESS_TOKEN_KEY
        settings_data['twitter']['CONSUMER_KEY']=CONSUMER_KEY
        settings_data['twitter']['CONSUMER_SECRET']=CONSUMER_SECRET
        settings_data['twitter']['ACCESS_TOKEN_SECRET']=ACCESS_TOKEN_SECRET
        saveSettings()

def addHashtag(tag):
    #add hashtag to settings
    global settings_data
    settings_data['twitter']['hashtags']=settings_data['twitter']['hashtags']+u' #'+unicode(tag, "utf-8")
    saveSettings()

def removeHashtag(tag):
    #return string of hashtags filling given character space
    from random import shuffle
    global settings_data
    hashtags=map(str, settings_data['twitter']['hashtags'].split('#')[1:])
    hashtags=map(str.strip, hashtags)
    if tag in hashtags:
        hashtags.remove(tag)
        rt=''
        for hashtag in hashtags:
            rt=rt+'#'+hashtag + ' '
        rt.strip()
        settings_data['twitter']['hashtags']=rt
        saveSettings()
        return True
    else:
        return False

def hashtagString(length=140,mode=0):
    #return string of hashtags filling given character space
    from random import shuffle
    global settings_data
    hashtags=settings_data['twitter']['hashtags'].split('#')[1:]
    hs=''
    ll=[]
    for item in hashtags:
        if len(item)+2<=length:
            ll.append(item)
    ll.sort(key=len)
    while length > len(ll[0]) and len(ll) > 0:
        il=[]
        for item in ll:
            if len(item)+2<=length:
                il.append(item)
        shuffle(il)
        if not len(il)==0:
            nh=il.pop()
            if len(nh)+2<=length:
                length=length-len(nh)-2
                hs=hs+'#'+nh.strip()+' '
                if nh in ll:
                    ll.remove(nh)
            if len(ll)<1:
                return str(hs).strip()
    return str(hs).strip()

def setDefaultTweet(dt='GIMP-Python tweet!'):
    global settings_data
    settings_data['twitter']['default_tweet']=unicode(dt, "utf-8")
    saveSettings()

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
        tweet_text = title + '\nby ' + settings_data['user']['author'] + ' ' + time_stamp[:4] + '\n'
    else:
        tweet_text = title + '\nby ' + settings_data['user']['author'] + ' ' + time_stamp[:4]
    tweet_text = tweet_text + '\n'+hashtagString(139-len(tweet_text))
    return tweet_text


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

