with open('input/6.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# input = [
#     'eedadn',
#     'drvtee',
#     'eandsr',
#     'raavrd',
#     'atevrs',
#     'tsrnev',
#     'sdttsa',
#     'rasrtv',
#     'nssdts',
#     'ntnada',
#     'svetve',
#     'tesnvt',
#     'vntsnd',
#     'vrdear',
#     'dvrsen',
#     'enarar'
# ]

# Part 1

messageLetters = [{} for x in range(len(input[0]))]

for position in range(len(messageLetters)):
    for line in input:
        letter = line[position]
        if letter in messageLetters[position]:
            messageLetters[position][letter] += 1
        else:
            messageLetters[position][letter] = 1

message = ''

for position in messageLetters:
    letters = sorted(position.items(), key=lambda x: (-x[1]))
    message += letters[0][0]

print message


# Part 2

messageLetters = [{} for x in range(len(input[0]))]

for position in range(len(messageLetters)):
    for line in input:
        letter = line[position]
        if letter in messageLetters[position]:
            messageLetters[position][letter] += 1
        else:
            messageLetters[position][letter] = 1

message = ''

for position in messageLetters:
    letters = sorted(position.items(), key=lambda x: (-x[1]))
    message += letters[-1][0]

print message
