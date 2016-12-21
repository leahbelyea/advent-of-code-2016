import math

input = 3018458

# Part 1

print int((input - 2**math.floor(math.log(input, 2))) * 2 + 1)


# Part 2

elves = range(1, input + 1)
currentElf = 0

while len(elves) > 1:
    if currentElf >= len(elves):
        currentElf = currentElf % len(elves)
    stealFrom = currentElf + (len(elves) / 2)
    del elves[stealFrom % len(elves)]
    if stealFrom <= len(elves):
        currentElf = (currentElf + 1) % len(elves)

print elves[0]
