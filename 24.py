import itertools

with open('input/24.txt', 'r') as f:
  input = [list(x.strip('\n')) for x in f.readlines()]

# input = [
#     list('###########'),
#     list('#0.1.....2#'),
#     list('#.#######.#'),
#     list('#4.......3#'),
#     list('###########')
# ]

graph = {}
pois = {}

for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == '#': continue
        if input[y][x] not in ['#', '.']: pois[input[y][x]] = (x,y)

        next = []
        if input[y+1][x] != '#':
            next.append((x,y+1))
        if input[y-1][x] != '#':
            next.append((x,y-1))
        if input[y][x+1] != '#':
            next.append((x+1,y))
        if input[y][x-1] != '#':
            next.append((x-1,y))

        graph[(x,y)] = next

def shortestDistance(graph, start, end):
    dist = {}
    prev = {}
    for node in graph.keys():
        dist[node] = float('inf')
        prev[node] = None
    dist[start] = 0
    nodes = graph.keys()
    while nodes:
        u = min(nodes, key=lambda x: dist[x])
        nodes.remove(u)
        neighbours = graph[u]
        for v in neighbours:
            if v in nodes:
                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
    return dist[end]

combinations = list(itertools.combinations(pois.keys(), 2))
graph2 = {}

for pair in combinations:
    start = pois[pair[0]]
    end = pois[pair[1]]
    distance = shortestDistance(graph, start, end)

    if pair[0] in graph2:
        graph2[pair[0]][pair[1]] = distance
    else:
        graph2[pair[0]] = {pair[1]: distance}

    if pair[1] in graph2:
        graph2[pair[1]][pair[0]] = distance
    else:
        graph2[pair[1]] = {pair[0]: distance}

def getPathLength(graph, path):
    length = 0
    for x in range(1, len(path)):
        u = path[x-1]
        v = path[x]
        length += graph[u][v]
    return length


# Part 1

start = '0'
others = graph2.keys()
others.remove(start)
paths = list(itertools.permutations(others, len(others)))
paths = map(lambda x: [start] + list(x), paths)

minLength = float('inf')
minPath = None
for path in paths:
    length = getPathLength(graph2, path)
    if length < minLength:
        minLength = length

print minLength


# Part 2

start = '0'
others = graph2.keys()
others.remove(start)
paths = list(itertools.permutations(others, len(others)))
paths = map(lambda x: [start] + list(x) + [start], paths)

minLength = float('inf')
minPath = None
for path in paths:
    length = getPathLength(graph2, path)
    if length < minLength:
        minLength = length

print minLength
