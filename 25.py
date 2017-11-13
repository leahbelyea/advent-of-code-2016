with open('input/25.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

def processInstruction(instruction, registers, currentInstruction):
    global signal
    instruction = instruction.split(' ')

    if len(instruction) > 2:
        [operation, param1, param2] = instruction
    else:
        [operation, param1] = instruction

    if operation == 'out':
        try:
            param1 = int(param1)
        except ValueError:
            param1 = registers[param1]
        signal += str(param1)

    elif operation == 'cpy':
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
requiredSignal = '01'*50
a = 0

while True:
    currentInstruction = 0
    registers = {
    'a': a,
    'b': 0,
    'c': 0,
    'd': 0
    }
    index = 0
    signal = ''
    while len(signal) < len(requiredSignal):
        index += 1
        [registers, currentInstruction] = processInstruction(input[currentInstruction], registers, currentInstruction)
        currentInstruction += 1
    if signal == requiredSignal:
      break
    a += 1

print a
