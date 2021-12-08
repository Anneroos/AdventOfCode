#08-12-2021
with open("input9.txt","r") as f:
    input = f.read()

def decompress1(string):
    if "(" in string:
        i = string.index("(")
        j = string.index(")")
        chars, repeat = [int(p) for p in string[i+1:j].split("x")]
        return string[0:i] + string[j+1:j+chars+1]*repeat + decompress1(string[j+1+chars:])
    else:
        return string

mydict = {}
def decompressedLength(string):
    if string in mydict.keys():
        return mydict[string]
    elif "(" in string:
        i = string.index("(")
        j = string.index(")")
        chars, repeat = [int(p) for p in string[i+1:j].split("x")]
        if string[j+1:j+chars+1] not in mydict.keys():
            mydict[string[j + 1:j + chars + 1]] = decompressedLength(string[j+1:j+chars+1])
        return i + mydict[string[j+1:j+chars+1]]*repeat + decompressedLength(string[j+1+chars:])
    else:
        return len(string)

print(f"Part 1: The length of the decompressed file is {len(decompress1(input))}.")
print(f"Part 2: The length of the decompressed file in the improved format is {decompressedLength(input)}.")