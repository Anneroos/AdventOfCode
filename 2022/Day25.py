with open("input25.txt") as f:
    SNAFUlist = f.read().split("\n")

def SNAFUtoDEC(snaf):
    symbols = {"0":0, "1":1, "2":2, "-":-1, "=":-2}
    l = snaf[-1]
    if len(snaf) == 1:
        return symbols[l]
    else:
        return symbols[l]+5*SNAFUtoDEC(snaf[0:(len(snaf)-1)])

def DECtoSNAF(dec):
    symbols = "012=-"
    r = dec % 5
    s = dec // 5

    if r in [3,4]:
        s += 1
    if s == 0:
        return symbols[r]
    else:
        return DECtoSNAF(s) + symbols[r]

sum = DECtoSNAF(sum([SNAFUtoDEC(l) for l in SNAFUlist]))
print(sum)

