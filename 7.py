import re

with open('input/7.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# input = [
#     'abba[mnop]qrst',
#     'abcd[bddb]xyyx',
#     'aaaa[qwer]tyui',
#     'ioxxoj[asdfgh]zxcvbn'
# ]

# input = [
#     'aba[bab]xyz',
#     'xyx[xyx]xyx',
#     'aaaxyx[kek]eke',
#     'zazbz[bzb]cdb',
#     'wef'
# ]

# Part 1

supportingIps = []

for ip in input:
    abbaMatches = re.findall('([a-z])([a-z])\\2\\1', ip) or []
    abbaValid = False
    for abba in abbaMatches:
        if abba[0] != abba[1]:
            abbaValid = True

    hasAbba = len(abbaMatches) > 0 and abbaValid

    abbaInBracketsMatches = re.findall('\[[a-z]*([a-z])([a-z])\\2\\1[a-z]*\]', ip) or []

    abbaInBracketsValid = False
    for abba in abbaInBracketsMatches:
        if abba[0] != abba[1]:
            abbaInBracketsValid = True

    hasAbbaInBrackets = len(abbaInBracketsMatches) > 0 and abbaInBracketsValid

    supportsTls = hasAbba and not hasAbbaInBrackets

    if supportsTls:
        supportingIps.append(ip)

print len(supportingIps)


# Part 2

supportingIps = []

for ip in input:
    ipSupernet = re.sub('\[[a-z]*\]', '', ip)
    abaMatches = re.findall('(?=([a-z])([a-z])\\1)', ipSupernet) or []

    print ip

    abas = []
    for aba in abaMatches:
        if aba[0] != aba[1]:
            if aba not in abas: abas.append(aba)

    for aba in abas:
        bab = re.findall('\[[a-z]*[%s][%s][%s][a-z]*\]' % (aba[1], aba[0], aba[1]), ip) or []
        if bab: supportingIps.append(ip)

print len(supportingIps)
