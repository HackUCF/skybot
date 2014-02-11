from util import http, hook

@hook.command(autohelp=False)
def dogecoin(inp, say=None):
    ".dogecoin -- gets current exchange rate for dogecoins"
    data = http.get_json("https://www.dogeapi.com/wow/?a=get_current_price&convert_to=USD&amount_doge=1")
    say("Current Doge: \x0307%s\x0f USD Current MegaDoge: \x0307%s\x0f USD" % (data, data*1000000))
