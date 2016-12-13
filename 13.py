input = 1350
gridSize = 60
end = (31,39)

# input = 10
# gridSize = 10
# end = (7,4)

def printGrid(grid):
    for row in grid:
        print ' '.join(row)

grid = [['#'] * gridSize for x in range(gridSize)]

for y in range(gridSize):
    for x in range(gridSize):
        if bin(x*x + 3*x + 2*x*y + y + y*y + input).count('1') % 2 == 0:
            grid[y][x] = '.'

graph = {}
for y in range(gridSize):
    for x in range(gridSize):
        if grid[y][x] == '#': continue
        next = []

        if x > 0 and grid[y][x-1] == '.':
            next.append((x-1,y))
        if x < gridSize - 1 and grid[y][x+1] == '.':
            next.append((x+1,y))
        if y > 0 and grid[y-1][x] == '.':
            next.append((x,y-1))
        if y < gridSize - 1 and grid[y+1][x] == '.':
            next.append((x,y+1))

        graph[(x,y)] = next

# Part 1

def findShortestPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path

    shortestPath = None
    for node in graph[start]:
        if node not in path:
            newPath = findShortestPath(graph, node, end, path)
            if newPath:
                if not shortestPath or len(newPath) < len(shortestPath):
                    shortestPath = newPath
    return shortestPath

path = findShortestPath(graph, (1,1), end)
print len(path) - 1

# for point in path:
#     x = point[0]
#     y = point[1]
#     grid[y][x] = '0'
#
# printGrid(grid)

# Part 2

def findPathUnder50(graph, start, end, path=[]):
    path = path + [start]
    if len(path) > 51:
        return None
    if start == end:
        return path

    shortestPath = None
    for node in graph[start]:
        if node not in path:
            newPath = findPathUnder50(graph, node, end, path)
            if newPath:
                if not shortestPath or len(newPath) < len(shortestPath):
                    shortestPath = newPath

    return shortestPath

potentialEnds = []
ends = []
for y in range(gridSize):
    for x in range(gridSize):
        if grid[y][x] == '.':
            potentialEnds.append((x,y))

for end in potentialEnds:
    if findPathUnder50(graph, (1,1), end):
        ends.append(end)

print len(ends)
