import binascii
from util import hook

@hook.command("b64")
@hook.command("b64enc")
@hook.command
def b64encode(inp):
	return inp.encode("base64")

@hook.command("b64dec")
@hook.command
def b64decode(inp):
	try:
		return inp.decode("base64")
	except binascii.Error, e:
		return "error decoding: " + str(e)


@hook.command("hex")
@hook.command("hexenc")
@hook.command
def hexencode(inp):
	return inp.encode("hex")

@hook.command("hexdec")
@hook.command
def hexdecode(inp):
	try:
		return inp.decode("hex")
	except TypeError, e:
		return "error decoding: " + str(e)


@hook.command("rot13".encode("rot13"))
@hook.command
def rot13(inp):
	return inp.encode("rot13")


@hook.command("bin")
@hook.command("binenc")
@hook.command
def binencode(inp):
	# http://codegolf.stackexchange.com/a/21039/9133
	return" ".join("".join("01"[ord(c)>>i&1]for i in range(7,-1,-1))for c in inp)

@hook.command("bindec")
@hook.command
def bindecode(inp):
	inp = inp.replace(" ", "")
	if len(inp) & 7:
		return "error: input length must be a multiple of 8"
	
	out = []
	try:
		for i in xrange(0, len(inp), 8):
			out.append(chr(int(inp[i:i+8], 2)))
	except ValueError, e:
		return "error: binary consists of only 0s and 1s"
	
	return "".join(out)
