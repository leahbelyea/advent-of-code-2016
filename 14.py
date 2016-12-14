from md5 import md5
import re

input = 'cuanljph'
# input = 'abc'

# Part 1

def findHashes(salt):
    index = 0
    potentialHashes = []
    correctHashes = []
    correctHashIndices = []

    while True:
        hash = md5(salt + str(index)).hexdigest()

        match5s = re.findall('([0-9]|[a-z])\\1\\1\\1\\1', hash)
        has5 = len(match5s) > 0
        if has5:
            for match5 in match5s:
                match3s = filter(lambda x: x['match'] == match5, potentialHashes)
                for match3 in match3s:
                    if index - match3['index'] <= 1000:
                        correctHashes.append(match3['hash'])
                        correctHashIndices.append(match3['index'])
                        if len(set(correctHashes)) >= 64:
                            return sorted(correctHashIndices)

        match3s = re.findall('([0-9]|[a-z])\\1\\1', hash)
        has3 = len(match3s) > 0
        if has3:
            potentialHashes.append({
                'hash': hash,
                'index': index,
                'match': match3s[0]
            })

        index += 1

print findHashes(input)[-1]


# Part 2

def findHashesPart2(salt):
    index = 0
    potentialHashes = []
    correctHashes = []
    correctHashIndices = []

    while True:
        hash = md5(salt + str(index)).hexdigest()

        for x in range(2016):
            hash = md5(hash).hexdigest()

        match5s = re.findall('([0-9]|[a-z])\\1\\1\\1\\1', hash)
        has5 = len(match5s) > 0
        if has5:
            for match5 in match5s:
                match3s = filter(lambda x: x['match'] == match5, potentialHashes)
                for match3 in match3s:
                    if index - match3['index'] <= 1000:
                        correctHashes.append(match3['hash'])
                        correctHashIndices.append(match3['index'])
                        if len(set(correctHashes)) >= 64:
                            return sorted(set(correctHashIndices))

        match3s = re.findall('([0-9]|[a-z])\\1\\1', hash)
        has3 = len(match3s) > 0
        if has3:
            potentialHashes.append({
                'hash': hash,
                'index': index,
                'match': match3s[0]
            })

        index += 1

print findHashesPart2(input)[-1]
