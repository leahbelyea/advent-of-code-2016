with open('input/8.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# input = [
#     'rect 3x2',
#     'rotate column x=1 by 1',
#     'rotate row y=0 by 4',
#     'rotate column x=1 by 1'
# ]

screen = [[0] * 50 for x in range(6)]
# screen = [[0] * 7 for x in range(3)]

# Part 1

def doInstruction(instruction, screen):
    operation = 'rect'
    if instruction.find('column') > 0: operation = 'column'
    if instruction.find('row') > 0: operation = 'row'

    if operation == 'rect':
        instruction = instruction.replace('rect ', '')
        [A, B] = (int(x) for x in instruction.split('x'))

        for column in range(A):
            for row in range(B):
                screen[row][column] = 1

        return screen

    elif operation == 'column':
        newScreen = map(list, screen)
        instruction = instruction.replace('rotate column x=', '')
        [A, B] = (int(x) for x in instruction.split(' by '))

        for row in range(len(screen)):
            nextRow = row + B if row + B < len(screen) else row + B - len(screen)

            if screen[row][A] == 1:
                newScreen[nextRow][A] = 1
            else:
                newScreen[nextRow][A] = 0

        return newScreen

    elif operation == 'row':
        newScreen = map(list, screen)
        instruction = instruction.replace('rotate row y=', '')
        [A, B] = (int(x) for x in instruction.split(' by '))

        for column in range(len(screen[0])):
            nextColumn = column + B if column + B < len(screen[0]) else column + B - len(screen[0])

            if screen[A][column] == 1:
                newScreen[A][nextColumn] = 1
            else:
                newScreen[A][nextColumn] = 0

        return newScreen


for instruction in input:
    screen = doInstruction(instruction, screen)

numPixels = 0
for row in screen:
    for column in row:
        if column == 1:
            numPixels += 1

print numPixels

# Part 2

def printScreen(screen):
    for row in screen:
        print row

printScreen(screen)
