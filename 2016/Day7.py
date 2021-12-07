# 6-12-2021
import re
with open("input7.txt", "r") as f:
    ips = f.read().splitlines()

def untangleIP(ip):
    realip = ""
    hypernet = ""
    brackets = 0
    for i in ip:
        if i == "[":
            brackets += 1
            realip += " "
        elif i == "]":
            brackets -=1
            hypernet += " "
        elif brackets == 0:
            realip += i
        else:
            hypernet += i
    return realip, hypernet

def containsABBA(string):
    s = re.findall(r'(\w)(?!\1)(\w)\2\1', string) # With negative lookahead! :)
    return True if len(s) > 0 else False

def checkTLSsupport(ip):
    realip, hypernet = untangleIP(ip)
    return containsABBA(realip) and not containsABBA(hypernet)

def checkSSLsupport(ip):
    realip, hypernet = untangleIP(ip)
    combined = realip + "#" + hypernet # at least now I now the order of things ;)
    s = re.findall(r'(\w)(?!\1)(\w)\1.*#.*\2\1\2', combined)
    return True if len(s) > 0 else False

print(f"Part 1: There are {sum([checkTLSsupport(ip) for ip in ips])} ips that support TLS!")
print(f"Part 2: There are {sum([checkSSLsupport(ip) for ip in ips])} ips that support SSL!")