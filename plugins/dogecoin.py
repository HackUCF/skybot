from util import http, hook

@hook.command(autohelp=False)
def dogecoin(inp, say=None):
    ".dogecoin -- gets current exchange rate for dogecoins"
    data = http.get_json("http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=182")
    data = data['return']
    data = data['markets']
    data = data['DOGE']
    say("Current Doge: \x0307%s\x0f USD" % (data['lasttradeprice'])
