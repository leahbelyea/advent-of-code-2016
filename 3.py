import re

with open('input/3.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]


# Part 1

possibleTriangles = []

for line in input:
    triangle = [int(line[0:3]), int(line[5:8]), int(line[10:13])]
    triangle.sort()
    if triangle[0] + triangle[1] > triangle[2]:
        possibleTriangles.append(triangle);

print len(possibleTriangles)


# Part 2

possibleTriangles = []

while len(input) >= 2:
    chunk = [input.pop(), input.pop(), input.pop()]
    chunk = map(lambda line: [int(line[0:3]), int(line[5:8]), int(line[10:13])], chunk)

    for x in range(3):
        triangle = [chunk[0][x], chunk[1][x], chunk[2][x]]
        triangle.sort()
        if triangle[0] + triangle[1] > triangle[2]:
            possibleTriangles.append(triangle)

print len(possibleTriangles)
