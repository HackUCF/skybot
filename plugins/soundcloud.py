import soundcloud
from util import hook
import re

# create a client object with your app credentials
client = soundcloud.Client(client_id='APIKEY')

soundcloud_re = (r'((https|http)?:\/\/(soundcloud.com)\/(.*)\/(.*))', re.I)

@hook.command
def soundcloud(search):
        if(search==''):
                return "Usage: .soundcloud *trackname*"
        # find all sounds of buskers licensed under 'creative commons share alike'
        track = client.get('/tracks', q=search, order='hotness', streamable='true', limit=1)[0]
        return "*" + track.user["username"] + "*" + " | " + track.title + " | " + track.permalink_url

@hook.command
def sc(search):
        return soundcloud(search)


@hook.regex(*soundcloud_re)
def soundcloud_url(match):
        #return match.group(0)
        track = client.get('/resolve', url=match.group(0))
        return "*" + track.user["username"] + "*" + " | " + track.title