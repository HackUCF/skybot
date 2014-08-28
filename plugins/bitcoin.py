from util import http, hook

@hook.command('buttcoin', autohelp=False)
@hook.command(autohelp=False)
def bitcoin(inp, say=None):
    ".bitcoin -- gets current exchange rate for bitcoins from BTC-e"
    data = http.get_json("https://btc-e.com/api/2/btc_usd/ticker")
    say("BTC/USD: \x0307{buy:.0f}\x0f - High: \x0307{high}\x0f"
        " - Low: \x0307{low}\x0f - Volume: {vol_cur:.0f}".format(**data['ticker']))


@hook.command('bitcat'. autohelp=False)
@hook.command(autohelp=False)
def bitcat(inp, say=None):
    ".bitcat -- ninjafish morning"
    data = http.get_json("https://btc-e.com/api/2/btc_usd/ticker")
    say("BTC/USD: \x0307{buy:.0f}\x0f - High: \x0307{high}\x0f"
        " - Low: \x0307{low}\x0f - Volume: {vol_cur:.0f}".format(**data['ticker']))
    data = http.get_json("http://catfacts-api.appspot.com/api/facts")
    catte = re.sub("cat", "catte", data['facts'][0])
    catte = re.sub("Cat", "Catte", catte)
    say("%s" % catte)
