with open('input/12.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# input = [
#     'cpy 41 a',
#     'inc a',
#     'inc a',
#     'dec a',
#     'jnz a 2',
#     'dec a'
# ]

def processInstruction(instruction, registers, currentInstruction):
    instruction = instruction.split(' ')

    if len(instruction) > 2:
        [operation, param1, param2] = instruction
    else:
        [operation, param1] = instruction

    if operation == 'cpy':
        try:
            param1 = int(param1)
        except ValueError:
            param1 = registers[param1]

        registers[param2] = int(param1)

    elif operation == 'inc':
        registers[param1] += 1

    elif operation == 'dec':
        registers[param1] -= 1

    elif operation == 'jnz':
        try:
            param1 = int(param1)
        except ValueError:
            param1 = registers[param1]
        if param1 == 0: return [registers, currentInstruction]

        currentInstruction += int(param2) - 1

    return [registers, currentInstruction]


# Part 1

registers = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0
}
currentInstruction = 0

while currentInstruction < len(input):
    [registers, currentInstruction] = processInstruction(input[currentInstruction], registers, currentInstruction)
    currentInstruction += 1

print registers


# Part 2

registers = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}
currentInstruction = 0

while currentInstruction < len(input):
    [registers, currentInstruction] = processInstruction(input[currentInstruction], registers, currentInstruction)
    currentInstruction += 1

print registers
