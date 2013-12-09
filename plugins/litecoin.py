from util import http, hook

@hook.command(autohelp=False)
def litecoin(inp, say=None):
    ".litecoin -- gets current exchange rate for litecoins from BTC-E"
    data = http.get_json("https://btc-e.com/api/2/ltc_usd/ticker")
    data = data['ticker']
    ticker = {
        'buy': data['buy'],
        'high': data['high'],
        'low': data['low'],
        'vol': '{:,.2f}'.format(data['vol_cur']),
    }
    say("Current: \x0307$%(buy)s\x0f - High: \x0307$%(high)s\x0f"
        " - Low: \x0307$%(low)s\x0f - Volume: %(vol)s LTC" % ticker)
