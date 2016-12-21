input = '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.'
rows = 40
# input = '.^^.^.^^^^'
# rows = 10

room = [input]
traps = ['^^.', '.^^', '^..', '..^']

def getRoom(room, rows, traps):
    for x in range(1, rows):
        prevRow = room[x - 1]
        row = []
        for column in range(len(prevRow)):
            if column == 0:
                block = '.' + ''.join(prevRow[column:column+2])
            elif column == len(prevRow) - 1:
                block = ''.join(prevRow[column-1:column+1]) + '.'
            else:
                block = ''.join(prevRow[column-1:column+2])

            if block in traps:
                row.append('^')
            else:
                row.append('.')

        room.append(row)

    return room

numSafeTiles = 0
for row in getRoom(room, rows, traps):
    numSafeTiles += row.count('.')

print numSafeTiles


# Part 2
room = [input]
rows = 400000

numSafeTiles = 0
for row in getRoom(room, rows, traps):
    numSafeTiles += row.count('.')

print numSafeTiles
