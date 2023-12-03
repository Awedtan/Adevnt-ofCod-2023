import re

sum = 0

while True:
    line = input()
    if line =='':
        break

    a = re.split(r'[:;,]', line)
    id = 0
    check = True
    max = [0,0,0]

    for chunk in a:
        chunk = chunk.strip()
        val = chunk.split()[0]
        col = chunk.split()[1]
        if col.isdigit():
            id = int(col)
        if val.isdigit():
            val = int(val)
            match col:
                case 'blue':
                    if val > max[0]:
                        max[0] = val
                case 'red':
                    if val > max[1]:
                        max[1] = val
                case 'green':
                    if val > max[2]:
                        max[2] = val
    sum += max[0] * max[1]* max[2]
print(sum)