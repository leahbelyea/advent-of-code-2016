input = '00101000101111010'

def generateData(data, length):
    while len(data) < length:
        a = data
        b = list(a)
        b = b[::-1]
        b = map(lambda x: str(1 - int(x)), b)
        data = a + '0' + ''.join(b)

    return data[:length]

def generateChecksum(data):
    checksum = []

    while True:
        pairs = [data[i:i+2] for i in range(0, len(data), 2)]

        for pair in pairs:
            if pair[0] == pair[1]:
                checksum.append('1')
            else:
                checksum.append('0')

        checksum = ''.join(checksum)
        if len(checksum) % 2 != 0:
            return checksum
        else:
            data = checksum
            checksum = []

# Part 1
length = 272
data = generateData(input, length)
print generateChecksum(data)


# Part 2
length = 35651584
data = generateData(input, length)
print generateChecksum(data)
