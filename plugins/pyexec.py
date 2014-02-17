import re

from util import hook, http


re_lineends = re.compile(r'[\r\n]*')


@hook.command
def python(inp):
    ".python <prog> -- executes python code <prog>"

    res = http.get("http://eval.appspot.com/eval", statement=inp).splitlines()

    if not res:
        return
    res[0] = re_lineends.split(res[0])[0]
    if res[0] != 'Traceback (most recent call last):':
        return res[0].decode('utf8', 'ignore')
    else:
        return res[-1].decode('utf8', 'ignore')
