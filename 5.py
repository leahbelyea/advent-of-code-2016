import md5

input= 'wtnhxymk'
# input = 'abc'

# Part 1

index = 0
password = ''

while True:
    hash = md5.new(input + str(index)).hexdigest()
    index += 1
    if hash[0:5] == '00000':
        password += hash[5]
    if len(password) == 8:
        break

print password


# Part 2

index = 0
password = ['-'] * 8


while True:
    hash = md5.new(input + str(index)).hexdigest()
    index += 1

    if hash[0:5] == '00000':
        position = int(hash[5], 16)
        if position > 7: continue
        print hash
        if password[position] == '-': password[position] = hash[6]
        print password

    if '-' not in password:
        break

print ''.join(password)
