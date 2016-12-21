import re

with open('input/21.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

input = [
    'swap position 4 with position 0',
    'swap letter d with letter b ',
    'reverse positions 0 through 4',
    # 'rotate left 1 step',
    # 'move position 1 to position 4',
    # 'move position 3 to position 0',
    # 'rotate based on position of letter b',
    # 'rotate based on position of letter d'
]

def doInstruction(password, instruction):
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
        return ''.join(password)
    elif op == 'rotate based':
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
        return ''.join(password)
    else:
        print 'Unknown instruction'
        return ''.join(password)


password = 'abcde'
input

for instruction in input:
    password = doInstruction(password, instruction)
    print password

# print password
