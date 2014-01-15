from util import http, hook

@hook.command(autohelp=False)
def dogecoin(inp, say=None):
    ".dogecoin -- gets current exchange rate for dogecoins"
    data = http.get_json("http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132")
    data = data['return']
    ticker = {
        'btc': data['markets']['DOGE']['lasttradeprice'],
    }
    say("Current Doge: \x0307%(btc)s\x0f BTC" % ticker)
