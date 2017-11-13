import re
import copy
import time

with open('input/22.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()][2:]

# input = [
#   '/dev/grid/node-x0-y0   10T    8T     2T   80%',
#   '/dev/grid/node-x0-y1   11T    6T     5T   54%',
#   '/dev/grid/node-x0-y2   32T   28T     4T   87%',
#   '/dev/grid/node-x1-y0    9T    7T     2T   77%',
#   '/dev/grid/node-x1-y1    8T    0T     8T    0%',
#   '/dev/grid/node-x1-y2   11T    7T     4T   63%',
#   '/dev/grid/node-x2-y0   10T    6T     4T   60%',
#   '/dev/grid/node-x2-y1    9T    8T     1T   88%',
#   '/dev/grid/node-x2-y2    9T    6T     3T   66%'
# ]

nodes = []
for line in input:
  nodeInfo = re.split(r'\s+', line)
  node = {
    'x': int(nodeInfo[0].split('-')[1][1:]),
    'y': int(nodeInfo[0].split('-')[2][1:]),
    'used': int(nodeInfo[2][:-1]),
    'avail': int(nodeInfo[3][:-1]),
    'isGoal': False
  }
  nodes.append(node)

viablePairs = []

for nodeA in nodes:
  for nodeB in nodes:
    isEmpty = nodeA['used'] == 0
    isSame = nodeA['x'] == nodeB['x'] and nodeA['y'] == nodeB['y']
    wouldFit = nodeA['used'] <= nodeB['avail']
    if (not isEmpty and not isSame and wouldFit):
      viablePairs.append((nodeA, nodeB))

print len(viablePairs)

# Part 2

def printGrid(nodes):
  maxX = 0
  maxY = 0
  for node in nodes:
    if node['x'] > maxX:
      maxX = node['x']
    if node['y'] > maxY:
      maxY = node['y']

  grid = []
  for line in range(maxY + 1):
    line = []
    for column in range(maxX + 1):
      line.append({})
    grid.append(line)

  for node in nodes:
    x = node['x']
    y = node['y']

    grid[y][x] = {
      'used': node['used'],
      'avail': node['avail'],
      'isGoal': x == maxX and y == 0
    }

  for line in grid:
    lineString = []
    for item in line:
      itemString = '{0}/{1}'.format(item['used'], item['used'] + item['avail'])
      if item['isGoal']:
        itemString = ' (G) '
      elif item['used'] > 400:
        itemString = '  #  '
      lineString.append(itemString)
    print ' '.join(lineString)

print '\n\n'
printGrid(nodes)
print '\n\nSolved manually from printed grid. Answer: 202'
