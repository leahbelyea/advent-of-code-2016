import re

with open('input/9.txt', 'r') as f:
  input = f.read().strip('\n')

# input = 'ADVENT'
# input = 'A(1x5)BC'
# input = '(3x3)XYZ'
# input = 'A(2x2)BCD(2x2)EFG'
# input = '(6x1)(1x3)A'
# input = 'X(8x2)(3x3)ABCY'


# Part 1 WRONG

decompressedInput = input
ignoreCount = 0
markerRegex = '\([0-9]+x[0-9]+\)'

while True:
    matches = re.findall(markerRegex, decompressedInput)
    if len(matches) > ignoreCount:
        marker = matches[ignoreCount]
        position = decompressedInput.find(marker) + len(marker)
        [letterCount, repeatCount] = [int(x) for x in marker.replace('(', '').replace(')', '').split('x')]
        repeatedChars = decompressedInput[position:position+letterCount]
        repeatedSeq = repeatedChars * repeatCount
        markersInRepeat = re.findall(markerRegex, repeatedSeq)
        ignoreCount += len(markersInRepeat)
        decompressedInput = decompressedInput.replace(marker + repeatedChars, repeatedSeq, 1)

    else:
        break

print len(decompressedInput)


# Part 1 RIGHT

decompressedInput = ''
currentLocation = 0

while currentLocation < len(input):
    if input[currentLocation] == '(':
        currentLocation += 1
        letterCount = ''
        repeatCount = ''
        while input[currentLocation] != 'x':
            letterCount += input[currentLocation]
            currentLocation += 1
        letterCount = int(letterCount)
        currentLocation += 1

        while input[currentLocation] != ')':
            repeatCount += input[currentLocation]
            currentLocation += 1
        repeatCount = int(repeatCount)
        currentLocation += 1

        repeatSeq = input[currentLocation:currentLocation + letterCount]
        currentLocation += letterCount

        decompressedInput += repeatSeq * repeatCount

    else:
        decompressedInput += input[currentLocation]
        currentLocation += 1

print len(decompressedInput)
