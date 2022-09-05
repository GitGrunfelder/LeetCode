part1 = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr
amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr
q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

# Using the str.method of maketrans() lets you assign a replacement for a char/dict of chars.
my_text = part1.maketrans({"a":'c', "b":'d', "c":'e', "d":'f', "e":'g',
                    "f":'h', "g":'i', "h":'j', "i":'k', "j":'l', "k":'m',
                    "l":'n', "m":'o', "n":'p', "o":'q', "p":'r', "q":'s',
                    "r":'t', "s":'u', "t":'v', "u":'w', "v":'x',
                    "w":'y', "x":'z', "y":'a', "z":'b', })

print(part1.translate(my_text)) # Then you call the translate function on the OG text with your translate rule you created.


url = "http://www.pythonchallenge.com/pc/def/map.html"
next_step = url.maketrans({"a":'c', "b":'d', "c":'e', "d":'f', "e":'g',
                    "f":'h', "g":'i', "h":'j', "i":'k', "j":'l', "k":'m',
                    "l":'n', "m":'o', "n":'p', "o":'q', "p":'r', "q":'s',
                    "r":'t', "s":'u', "t":'v', "u":'w', "v":'x',
                    "w":'y', "x":'z', "y":'a', "z":'b', })
print(url.translate(next_step))