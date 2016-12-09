import re

with open('input/9.txt', 'r') as f:
  input = f.read().strip('\n')

# input = 'ADVENT'
# input = 'A(1x5)BC'
# input = '(3x3)XYZ'
# input = 'A(2x2)BCD(2x2)EFG'
# input = '(6x1)(1x3)A'
# input = 'X(8x2)(3x3)ABCY'

decompressedInput = input
ignoreCount = 0
markerRegex = '\([0-9]+x[0-9]+\)'
print input

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

print decompressedInput
print len(decompressedInput)
