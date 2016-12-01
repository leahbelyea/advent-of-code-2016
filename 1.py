with open('input/1.txt', 'r') as f:
  input = f.read()

instructions = input.split(', ')
# instructions = ['L2', 'R3']
# instructions = ['R2', 'R2', 'R2']
# instructions = ['R5', 'L5', 'R5', 'R3']

start = [0, 0]
currentLocation = start
currentDirection = 0

for instruction in instructions:
    turn = instruction[0]
    steps = int(instruction[1:])

    if turn == 'L':
        currentDirection = currentDirection - 90
    if turn == 'R':
        currentDirection = currentDirection + 90
    if currentDirection >= 360:
        currentDirection = currentDirection - 360
    if currentDirection < 0:
        currentDirection = currentDirection + 360
    print turn
    print currentDirection

    print instruction
    if currentDirection == 0:
        currentLocation = [currentLocation[0] + steps, currentLocation[1]]
    if currentDirection == 90:
        currentLocation = [currentLocation[0], currentLocation[1] + steps]
    if currentDirection == 180:
        currentLocation = [currentLocation[0] - steps, currentLocation[1]]
    if currentDirection == 270:
        currentLocation = [currentLocation[0], currentLocation[1] - steps]

    print currentLocation

taxicabDistance = abs(currentLocation[0]) + abs(currentLocation[1])
# print currentLocation

print taxicabDistance
