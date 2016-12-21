with open('input/20.txt', 'r') as f:
    input = [x.strip('\n') for x in f.readlines()]
maxIp = 4294967295

# Part 1

rangeStarts = []
rangeEnds = []

for index, ipRange in enumerate(input):
    ipRange = ipRange.split('-')
    rangeStarts.append((int(ipRange[0]), index))
    rangeEnds.append(int(ipRange[1]))

rangeStarts.sort()

index = 0
while True:
    start = rangeStarts[index]
    end = rangeEnds[start[1]]
    nextStart = rangeStarts[index+1]
    nextEnd = rangeEnds[rangeStarts[index+1][1]]

    if nextStart[0] > end + 1:
        print end + 1
        break

    index += 1


# Part 2

numIps = 0
ranges = []

for ipRange in input:
    ipRange = ipRange.split('-')
    ranges.append((int(ipRange[0]), int(ipRange[1])))

ranges.sort()

while True:
    for x in range(len(ranges) - 1):
        if ranges[x] == None: continue
        ipRange = ranges[x]
        nextIpRange = ranges[x + 1]
        start = ipRange[0]
        end = ipRange[1]
        nextStart = nextIpRange[0]
        nextEnd = nextIpRange[1]


        contains = nextStart >= start and nextEnd <= end
        overlaps = nextStart >= start and nextStart <= end and nextEnd > end

        if contains:
            ranges[x + 1] = None

        elif overlaps:
            newIpRange = (start, nextEnd)
            ranges[x + 1] = None
            ranges[x] = newIpRange

    newRanges = filter(lambda x: x, ranges)
    if len(newRanges) == len(ranges):
        ranges = newRanges
        break
    ranges = newRanges

for x in range(len(ranges) - 1):
    ipRange = ranges[x]
    nextIpRange = ranges[x + 1]
    start = ipRange[0]
    end = ipRange[1]
    nextStart = nextIpRange[0]
    nextEnd = nextIpRange[1]

    if nextStart > end + 1:
        numIps += (nextStart - end - 1)

    if x == len(ranges) - 2:
        numIps += (maxIp - nextEnd)

print numIps
