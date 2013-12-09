from util import hook
import datetime

@hook.command(autohelp=False)
def rebecca(inp, say=None):
    ".rebecca -- count the days until Rebecca Black is 18"
    today = datetime.date.today()
    birthday = datetime.date(2015, 6, 20)
    diff = birthday - today
    say("%s days until Rebecca Black is 18!" % diff.days)
