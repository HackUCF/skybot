import soundcloud
from util import hook

# create a client object with your app credentials
client = soundcloud.Client(client_id='APIKEY')

@hook.command
def soundcloud(search):
	track = client.get('/tracks', q=search, order='hotness', streamable='true', limit=1)[0]
	return track.title + " | " + track.permalink_url
