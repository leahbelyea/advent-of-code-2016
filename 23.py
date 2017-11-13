import copy

with open('input/23.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# input = [
#   'cpy 2 a',
#   'tgl a',
#   'tgl a',
#   'tgl a',
#   'cpy 1 a',
#   'dec a',
#   'dec a'
# ]

def processInstruction(registers, currentInstruction, instructions):
  instruction = instructions[currentInstruction].split(' ')

  if instruction == ['jnz', 'c', '-2'] and registers['c'] != 0:
    registers['a'] += registers['c']
    registers['c'] = 0
    return [registers, currentInstruction, instructions]
  elif instruction == ['jnz', 'd', '-5'] and registers['d'] != 0:
    registers['c'] = registers['b']
    registers['a'] += registers['c']*registers['d']
    registers['c'] = 0
    registers['d'] = 0
    return [registers, currentInstruction, instructions]

  if len(instruction) > 2:
    [operation, param1, param2] = instruction
  else:
    [operation, param1] = instruction

  if operation == 'tgl':
    try:
      param1 = int(param1)
    except ValueError:
      param1 = registers[param1]
    if currentInstruction + param1 < len(instructions):
      newInstruction = instructions[currentInstruction + param1].split(' ')
      if newInstruction[0] == 'inc':
        newInstruction[0] = 'dec'
      elif len(newInstruction) == 2:
        newInstruction[0] = 'inc'
      elif newInstruction[0] == 'jnz':
        newInstruction[0] = 'cpy'
      else:
        newInstruction[0] = 'jnz'

      newInstruction = ' '.join(newInstruction)
      instructions[currentInstruction + param1] = newInstruction

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
    try:
      param2 = int(param2)
    except ValueError:
      param2 = registers[param2]
    if param1 == 0: return [registers, currentInstruction, instructions]

    currentInstruction += int(param2) - 1

  return [registers, currentInstruction, instructions]

# Part 1

registers = {
  'a': 7,
  'b': 0,
  'c': 0,
  'd': 0
}
instructions = copy.copy(input)
currentInstruction = 0

while currentInstruction < len(instructions):
  [registers, currentInstruction, instructions] = processInstruction(registers, currentInstruction, instructions)
  currentInstruction += 1

print registers['a']

# Part 2
registers = {
  'a': 12,
  'b': 0,
  'c': 0,
  'd': 0
}
instructions = copy.copy(input)
currentInstruction = 0

while currentInstruction < len(instructions):
  [registers, currentInstruction, instructions] = processInstruction(registers, currentInstruction, instructions)
  currentInstruction += 1

print registers['a']
