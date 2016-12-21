import re

with open('input/21.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# Part 1

def rotateBased(index, password):
    rotationTimes = index + 1
    if index >= 4: rotationTimes += 1
    for x in range(rotationTimes):
        password.insert(0, password.pop())
    return password

def doInstruction(password, instruction, reverse=False):
    op = re.findall('^[a-z]+\s[a-z]+', instruction)[0]
    instruction = instruction.split(' ')
    password = list(password)

    if op == 'swap position':
        index1 = int(instruction[2])
        index2 = int(instruction[5])
        char1 = password[index1]
        char2 = password[index2]
        password[index1] = char2
        password[index2] = char1
        return ''.join(password)

    elif op == 'swap letter':
        index1 = password.index(instruction[2])
        index2 = password.index(instruction[5])
        char1 = password[index1]
        char2 = password[index2]
        password[index1] = char2
        password[index2] = char1
        return ''.join(password)

    elif op in ['rotate left', 'rotate right']:
        direction = instruction[1]
        if reverse:
            direction = 'left' if direction == 'right' else 'right'

        steps = int(instruction[2])
        if direction == 'left':
            for x in range(steps):
                password.insert(len(password)-1, password.pop(0))
        elif direction == 'right':
            for x in range(steps):
                password.insert(0, password.pop())

        return ''.join(password)

    elif op == 'rotate based':
        char = instruction[6]
        index = password.index(char)

        if reverse:
            for steps in range(1, len(password)+1):
                rotatedLeft = list(password)
                for x in range(steps):
                    rotatedLeft.insert(len(rotatedLeft)-1, rotatedLeft.pop(0))
                rotatedIndex = rotatedLeft.index(char)
                rotatedRight = rotateBased(rotatedIndex, list(rotatedLeft))
                if rotatedRight == password:
                    return ''.join(rotatedLeft)
        else:
            pssword = rotateBased(index, password)
            return ''.join(password)

    elif op == 'reverse positions':
        index1 = int(instruction[2])
        index2 = int(instruction[4])
        start = password[0:index1]
        end = password[index2+1:]
        middle = password[index1:index2+1]
        middle.reverse()
        return ''.join(start + middle + end)

    elif op == 'move position':
        index1 = int(instruction[5]) if reverse else int(instruction[2])
        index2 = int(instruction[2]) if reverse else int(instruction[5])
        char = password.pop(index1)
        password.insert(index2, char)
        return ''.join(password)

    else:
        print 'Unknown instruction'
        return ''.join(password)


password = 'abcdefgh'

for instruction in input:
    password = doInstruction(password, instruction)

print password


# Part 2

password = 'fbgdceah'

input.reverse()

for instruction in input:
    password = doInstruction(password, instruction, True)

print password
