import soundcloud
from util import hook
import re

@hook.api_key("soundcloud")
class scclient(object):
	def __init__(self, func):
		self.func = func
	
	def __call__(self, *args, **kwargs):
		kwargs["client"] = soundcloud.Client(client_id=kwargs.pop("api_key"))
		return self.func(*args, **kwargs)


def pretty_duration(ms):
	s = ms / 1000
	m = s / 60
	s %= 60
	h = m / 60
	m %= 60
	
	if h:
		return "%d:%.2d:%.2d" % (h, m, s)
	
	return "%d:%.2d" % (m, s)

def pretty_info(track):
	return "*" + track.user["username"] + "* " + " | ".join((track.title, pretty_duration(track.duration), track.permalink_url))

@scclient
@hook.command("soundcloud")
@hook.command
def sc(inp, client=None):
	"Usage: .soundcloud trackname"
	track = client.get('/tracks', q=inp.strip(), order='hotness', streamable='true', limit=1)[0]
	return pretty_info(track)

@scclient
@hook.regex(r'^((?:https?://)soundcloud\.com/[^/]+/[^/]+)', re.I)
def soundcloud_url(match, client=None):
	track = client.get('/resolve', url=match.group(0))
	return pretty_info(track)


if __name__ == "__main__":
	print sc(raw_input(".sc "))
