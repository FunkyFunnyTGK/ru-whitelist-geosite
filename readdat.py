import sys
b = open(sys.argv[1], "rb").read()
def rv(b, i):
    n = s = 0
    while True:
        x = b[i]; i += 1; n |= (x & 0x7F) << s; s += 7
        if x < 0x80: return n, i
def msgs(b):
    i = 0
    while i < len(b):
        k, i = rv(b, i); f, w = k >> 3, k & 7
        if w == 2: l, i = rv(b, i); yield f, b[i:i+l]; i += l
        else: v, i = rv(b, i); yield f, v
for f, s in msgs(b):
    code, doms = None, []
    for g, x in msgs(s):
        if g == 1: code = x.decode()
        else: doms.append(dict(msgs(x)))
    print(code, len(doms), [(d.get(1, 0), d[2].decode()) for d in doms[:3]])
