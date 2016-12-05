import re

with open('input/4.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# input = [
#     'aaaaa-bbb-z-y-x-123[abxyz]',
#     'a-b-c-d-e-f-g-h-987[abcde]',
#     'not-a-real-room-404[oarel]',
#     'totally-real-room-200[decoy]'
# ]

# input = [
#     'qzmt-zixmtkozy-ivhz-343[zimth]'
# ]

# Part 1

realRooms = []
idSum = 0

def getChecksum(name):
    letters = {}

    for letter in name:
        if not re.match('[a-z]', letter): continue

        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    formattedLetters = letters.items()
    formattedLetters = sorted(formattedLetters, key=lambda x: (-x[1], x[0]))

    checksum = ''
    for x in range(5):
        checksum += formattedLetters[x][0]

    return checksum

for room in input:
    matches = re.findall('([a-z0-9\-]+)\[([a-z]+)\]', room)[0]
    name = matches[0]
    checksum = matches[1]
    sectorID = int(name.split('-')[-1])

    if getChecksum(name) == checksum:
        idSum += sectorID
        realRooms.append(name)

print idSum


# Part 2

def decryptName(name, number):
    decryptedName = ''

    for letter in name:
        if letter == ' ':
            newLetter = letter
        else:
            ascii = ord(letter)
            newAscii = ascii + (number % 26)
            if newAscii > 122: newAscii -= 26
            newLetter = chr(newAscii)

        decryptedName += newLetter

    return decryptedName

for room in input:
    matches = re.findall('([a-z0-9\-]+)\[([a-z]+)\]', room)[0]
    name = ' '.join(matches[0].split('-')[0:-1])
    sectorID = int(matches[0].split('-')[-1])

    if decryptName(name, sectorID) == 'northpole object storage':
        print sectorID
        break
