from util import http, hook
import re

@hook.command('cat', autohelp=False)
@hook.command(autohelp=False)
def cat(inp, say=None):
    ".cat -- gets cat facts"
    data = http.get_json("http://catfacts-api.appspot.com/api/facts")
    say("%s" % data['facts'][0])

@hook.command('catte', autohelp=False)
@hook.command(autohelp=False)
def cattes(inp, say=None):
    ".catte -- gets catte facts"
    data = http.get_json("http://catfacts-api.appspot.com/api/facts")
    catte = re.sub("cat", "catte", data['facts'][0])
    catte = re.sub("Cat", "Catte", catte)
    say("%s" % catte)
