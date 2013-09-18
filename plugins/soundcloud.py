import soundcloud
from util import hook

# create a client object with your app credentials
client = soundcloud.Client(client_id='APIKEY')

@hook.command
def soundcloud(search):
	# find all sounds of buskers licensed under 'creative commons share alike'
	track = client.get('/tracks', q=search, order='hotness', streamable='true', limit=1)[0]
	return track.title + " | " + track.permalink_url
