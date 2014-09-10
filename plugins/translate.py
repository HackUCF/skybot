'''
A Google API key is required and retrieved from the bot config file.
Since December 1, 2011, the Google Translate API is a paid service only.
'''

import htmlentitydefs
import urllib2
import re

from util import hook, http

api_key = ""

########### from http://effbot.org/zone/re-sub.htm#unescape-html #############


def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text  # leave as is

    return re.sub("&#?\w+;", fixup, text)

##############################################################################

def goog_trans(text, tlang="auto", slang="auto"):
    '''Return the translation using google translate
    you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
    if you don't define anything it will detect it or use english by default
    Example:
    print(translate("salut tu vas bien?", "en"))
    hello you alright?'''
    agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
    before_trans = 'class="t0">'
    link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (tlang, slang, text.replace(" ", "+"))
    request = urllib2.Request(link, headers=agents)
    page = urllib2.urlopen(request).read()
    result = page[page.find(before_trans)+len(before_trans):]
    result = result.split("<")[0]
    return result


def match_language(fragment):
    fragment = fragment.lower()
    for short, _ in lang_pairs:
        if fragment in short.lower().split():
            return short.split()[0]

    for short, full in lang_pairs:
        if fragment in full.lower():
            return short.split()[0]

    return None


@hook.command
def translate(inp, bot=None):
    '.translate [source language [target language]] <sentence> -- translates' \
    ' <sentence> from source language (default autodetect) to target' \
    ' language (default English) using Google Translate'

    args = inp.split(' ', 2)

    try:
        if len(args) >= 2:
            sl = match_language(args[0])
            if not sl:
                return goog_trans(inp)
            if len(args) == 2:
                return goog_trans(args[1], slang=sl)
            if len(args) >= 3:
                tl = match_language(args[1])
                if not tl:
                    if sl == 'en':
                        return 'unable to determine desired target language'
                    return goog_trans(args[1] + ' ' + args[2], sl, 'en')
                return goog_trans(args[2], sl, tl)
        return goog_trans(inp, '', 'en')
    except IOError, e:
        return e


languages = 'ja fr de ko ru zh'.split()
language_pairs = zip(languages[:-1], languages[1:])


def babel_gen(inp):
    for language in languages:
        inp = inp.encode('utf8')
        trans = goog_trans(inp, 'en', language).encode('utf8')
        inp = goog_trans(trans, language, 'en')
        yield language, trans, inp


@hook.command
def babel(inp, bot=None):
    ".babel <sentence> -- translates <sentence> through multiple languages"

    if not hasapikey(bot):
        return None

    try:
        return list(babel_gen(inp))[-1][2]
    except IOError, e:
        return e


@hook.command
def babelext(inp, bot=None):
    ".babelext <sentence> -- like .babel, but with more detailed output"

    if not hasapikey(bot):
        return None

    try:
        babels = list(babel_gen(inp))
    except IOError, e:
        return e

    out = u''
    for lang, trans, text in babels:
        out += '%s:"%s", ' % (lang, text.decode('utf8'))

    out += 'en:"' + babels[-1][2].decode('utf8') + '"'

    if len(out) > 300:
        out = out[:150] + ' ... ' + out[-150:]

    return out

def hasapikey(bot):
    api_key = bot.config.get("api_keys", {}).get("googletranslate", None)
    return api_key

lang_pairs = [
    ("no", "Norwegian"),
    ("it", "Italian"),
    ("ht", "Haitian Creole"),
    ("af", "Afrikaans"),
    ("sq", "Albanian"),
    ("ar", "Arabic"),
    ("hy", "Armenian"),
    ("az", "Azerbaijani"),
    ("eu", "Basque"),
    ("be", "Belarusian"),
    ("bg", "Bulgarian"),
    ("ca", "Catalan"),
    ("zh-CN zh", "Chinese"),
    ("hr", "Croatian"),
    ("cs", "Czech"),
    ("da", "Danish"),
    ("nl", "Dutch"),
    ("en", "English"),
    ("et", "Estonian"),
    ("tl", "Filipino"),
    ("fi", "Finnish"),
    ("fr", "French"),
    ("gl", "Galician"),
    ("ka", "Georgian"),
    ("de", "German"),
    ("el", "Greek"),
    ("ht", "Haitian Creole"),
    ("iw", "Hebrew"),
    ("hi", "Hindi"),
    ("hu", "Hungarian"),
    ("is", "Icelandic"),
    ("id", "Indonesian"),
    ("ga", "Irish"),
    ("it", "Italian"),
    ("ja jp jpn", "Japanese"),
    ("ko", "Korean"),
    ("lv", "Latvian"),
    ("lt", "Lithuanian"),
    ("mk", "Macedonian"),
    ("ms", "Malay"),
    ("mt", "Maltese"),
    ("no", "Norwegian"),
    ("fa", "Persian"),
    ("pl", "Polish"),
    ("pt", "Portuguese"),
    ("ro", "Romanian"),
    ("ru", "Russian"),
    ("sr", "Serbian"),
    ("sk", "Slovak"),
    ("sl", "Slovenian"),
    ("es", "Spanish"),
    ("sw", "Swahili"),
    ("sv", "Swedish"),
    ("th", "Thai"),
    ("tr", "Turkish"),
    ("uk", "Ukrainian"),
    ("ur", "Urdu"),
    ("vi", "Vietnamese"),
    ("cy", "Welsh"),
    ("yi", "Yiddish")
]
