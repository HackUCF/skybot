from util import http, hook

@hook.command(autohelp=False)
def dogecoin(inp, say=None):
    ".dogecoin -- gets current exchange rate for dogecoins"
    data = http.get_json("http://dogecoin.org/api/market.json")
    data = data['ticker']
    ticker = {
        'btc': data['megadoge']['btc'],
	'usd': data['megadoge']['usd']
    }
    say("Current Megadoge: \x0307%(btc)s\x0f BTC \x0307%(usd)s\x0f USD" % ticker)
