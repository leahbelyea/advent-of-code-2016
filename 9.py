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
# print input

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



# import re
# data = input
#
# def findall(sub, string):
#     index = 0 - len(sub)
#     try:
#         while True:
#             index = string.index(sub, index + len(sub))
#             yield index
#     except ValueError:
#         pass
#
# def str_in_list(string, lst):
#     return any(string in i for i in lst)
#
# def find_marks(s):
#     marks = []
#     raw_marks = re.findall('\(.*?\)',s)
#     for mark in raw_marks:
#         mlength = len(mark)
#         idx = min([i for i in findall(mark, s) if i not in [x[1] for x in marks]])
#         length = int(mark.split("x")[0][1:])
#         times = int(mark.split("x")[1][:-1])
#         if not str_in_list(s[idx:idx + len(mark)],[s[i[1] + i[4]:i[1] + i[2]+ i[4]] for i in marks]):
#             marks.append((mark, idx, length, times, mlength))
#     return marks
#
# def decomp(s):
#     new_str = ""
#     m =  find_marks(s)
#     mark_indexes = [i[1] for i in m]
#     cursor = 0
#     while cursor < len(s):
#         if cursor in mark_indexes:
#             j = mark_indexes.index(cursor)
#             cursor += m[j][4]
#             new_str += s[cursor:cursor + m[j][2]]*m[j][3]
#             cursor += m[j][2]
#         else:
#             new_str += s[cursor]
#             cursor += 1
#     return new_str
#
# print len(data.strip())
# print len(decomp(data.strip()))
