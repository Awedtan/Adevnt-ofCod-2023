import re

sum = 0
f = open('input.txt', 'r')

while True:
    line = f.readline()
    if line =='':
        break

    a = re.split(r'[:;,]', line)
    id = 0
    check = True

    for chunk in a:
        chunk = chunk.strip()
        val = chunk.split()[0]
        col = chunk.split()[1]
        if col.isdigit():
            id = int(col)
        if val.isdigit():
            match col:
                case 'blue':
                    if int(val) > 14:
                        check = False
                case 'red':
                    if int(val) > 12:
                        check = False
                case 'green':
                    if int(val) > 13:
                        check = False
    if check:
        sum += id
print(sum)