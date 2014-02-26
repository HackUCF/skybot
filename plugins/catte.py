from util import http, hook
import re

@hook.command('catte', autohelp=False)
@hook.command(autohelp=False)
def cattes(inp, say=None):
    ".cattes -- gets cate facts"
    data = http.get_json("http://catfacts-api.appspot.com/api/facts")
    say("%s" % data['facts'][0].replace("cat","catte"))
