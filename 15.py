import re

with open('input/15.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# input = [
#     'Disc #1 has 5 positions; at time=0, it is at position 4.',
#     'Disc #2 has 2 positions; at time=0, it is at position 1.'
# ]

class Disc:
    def __init__(self, id, positions, positionat0):
        self.id = int(id)
        self.positions = int(positions)
        self.positionAt0 = int(positionAt0)

    def positionAtTime(self, startTime):
        return (self.positionAt0 + self.id + startTime) % self.positions

discs = []
for disc in input:
    [id, positions, positionAt0] = re.findall('.*#([0-9]+).* ([0-9]+) positions.*position ([0-9]+).', disc)[0]
    discs.append(Disc(id, positions, positionAt0))


# Part 1

time = 0
while True:
    capsuleFalls = True
    for disc in discs:
        if disc.positionAtTime(time) != 0:
            capsuleFalls = False

    if capsuleFalls:
        break
    else:
        time += 1

print time


# Part 2

discs.append(Disc(7, 11, 0))

time = 0
while True:
    capsuleFalls = True
    for disc in discs:
        if disc.positionAtTime(time) != 0:
            capsuleFalls = False

    if capsuleFalls:
        break
    else:
        time += 1

print time
