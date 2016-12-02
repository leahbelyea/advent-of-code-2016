with open('input/2.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# input = [
#     'ULL',
#     'RRDDD',
#     'LURDL',
#     'UUUUD'
# ]


# Part 1

keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

code = []

def getDigitPosition(line, currentPosition = [1,1]):
    while len(line) > 0:
        currentPosition = doInstruction(line[0], currentPosition)
        line = line[1:]

    return currentPosition


def doInstruction(instruction, currentPosition):
    if instruction == 'U':
        if currentPosition[0] == 0: return currentPosition
        return [currentPosition[0] - 1, currentPosition[1]]
    if instruction == 'D':
        if currentPosition[0] == 2: return currentPosition
        return [currentPosition[0] + 1, currentPosition[1]]
    if instruction == 'L':
        if currentPosition[1] == 0: return currentPosition
        return [currentPosition[0], currentPosition[1] - 1]
    if instruction == 'R':
        if currentPosition[1] == 2: return currentPosition
        return [currentPosition[0], currentPosition[1] + 1]

digitPosition = None

for line in input:
    digitPosition = getDigitPosition(line, digitPosition) if digitPosition else getDigitPosition(line);
    code.append(keypad[digitPosition[0]][digitPosition[1]])

print ''.join(str(x) for x in code)


# Part 2

keypad = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, 'A', 'B', 'C', 0],
    [0, 0, 'D', 0, 0]
]

code = []

def getDigitPosition(line, currentPosition = [2,0]):
    while len(line) > 0:
        currentPosition = doInstruction(line[0], currentPosition)
        line = line[1:]

    return currentPosition


def doInstruction(instruction, currentPosition):
    if instruction == 'U':
        edgeOfKeypad = currentPosition[0] == 0
        if edgeOfKeypad: return currentPosition

        isZero = keypad[currentPosition[0] - 1][currentPosition[1]] == 0
        if isZero: return currentPosition

        return [currentPosition[0] - 1, currentPosition[1]]

    if instruction == 'D':
        edgeOfKeypad = currentPosition[0] == 4
        if edgeOfKeypad: return currentPosition

        isZero = keypad[currentPosition[0] + 1][currentPosition[1]] == 0
        if isZero: return currentPosition

        return [currentPosition[0] + 1, currentPosition[1]]

    if instruction == 'L':
        edgeOfKeypad = currentPosition[1] == 0
        if edgeOfKeypad: return currentPosition

        isZero = keypad[currentPosition[0]][currentPosition[1] - 1] == 0
        if isZero: return currentPosition

        return [currentPosition[0], currentPosition[1] - 1]

    if instruction == 'R':
        edgeOfKeypad = currentPosition[1] == 4
        if edgeOfKeypad: return currentPosition

        isZero = keypad[currentPosition[0]][currentPosition[1] + 1] == 0
        if isZero: return currentPosition

        return [currentPosition[0], currentPosition[1] + 1]

digitPosition = None

for line in input:
    digitPosition = getDigitPosition(line, digitPosition) if digitPosition else getDigitPosition(line);
    code.append(keypad[digitPosition[0]][digitPosition[1]])

print ''.join(str(x) for x in code)
