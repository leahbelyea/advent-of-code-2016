from md5 import md5

input = 'pslxynzg'
# input = 'ihgpwlah'
# input = 'kglvqrro'
# input = 'ulqzkmiv'

#########
#A|B|C|D#
#-#-#-#-#
#E|F|G|H#
#-#-#-#-#
#I|J|K|L#
#-#-#-#-#
#M|N|O|P
####### V

rooms = {
    'A': [('D', 'E'), ('R', 'B')],
    'B': [('D', 'F'), ('R', 'C'), ('L', 'A')],
    'C': [('D', 'G'), ('R', 'D'), ('L', 'B')],
    'D': [('D', 'H'), ('L', 'C')],
    'E': [('D', 'I'), ('R', 'F'), ('U', 'A')],
    'F': [('D', 'J'), ('R', 'G'), ('L', 'E'), ('U', 'B')],
    'G': [('D', 'K'), ('R', 'H'), ('L', 'F'), ('U', 'C')],
    'H': [('D', 'L'), ('L', 'G'), ('U', 'D')],
    'I': [('D', 'M'), ('R', 'J'), ('U', 'E')],
    'J': [('D', 'N'), ('R', 'K'), ('L', 'I'), ('U', 'F')],
    'K': [('D', 'O'), ('R', 'L'), ('L', 'J'), ('U', 'G')],
    'L': [('D', 'P'), ('L', 'K'), ('U', 'H')],
    'M': [('R', 'N'), ('U', 'I')],
    'N': [('R', 'O'), ('L', 'M'), ('U', 'J')],
    'O': [('R', 'P'), ('L', 'N'), ('U', 'K')],
    'P': []
}

def isValidMove(move, path):
    hash = md5(input + ''.join(path)).hexdigest()
    validChars = ['b', 'c', 'd', 'e', 'f']
    hashPosition = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    return hash[hashPosition[move]] in validChars


# Part 1

def findShortestPath(graph, start, end, path=[]):
    if start[0]:
        path = path + [start[0]]
    if start[1] == end:
        return path

    shortestPath = None
    validMoves = [x for x in graph[start[1]] if isValidMove(x[0], path)]
    for node in validMoves:
        if node not in path:
            newPath = findShortestPath(graph, node, end, path)
            if newPath:
                if not shortestPath or len(newPath) < len(shortestPath):
                    shortestPath = newPath
    return shortestPath


path = findShortestPath(rooms, (None, 'A'), 'P')
print ''.join(path)


# Part 2

def findLongestPath(graph, start, end, path=[]):
    if start[0]:
        path = path + [start[0]]
    if start[1] == end:
        return path

    longestPath = None
    validMoves = [x for x in graph[start[1]] if isValidMove(x[0], path)]
    for node in validMoves:
        if node not in path:
            newPath = findLongestPath(graph, node, end, path)
            if newPath:
                if not longestPath or len(newPath) > len(longestPath):
                    longestPath = newPath
    return longestPath


path = findLongestPath(rooms, (None, 'A'), 'P')
print len(path)
