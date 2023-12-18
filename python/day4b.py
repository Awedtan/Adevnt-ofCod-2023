sum=0
copies = [0]
while True:
    line = input()
    if line == '':
        break

    line = line[line.index(':')+1:].split('|')
    win = [num for num in line[0].strip().split()]
    my = [num for num in line[1].strip().split()]

    copy = copies.pop(0) if len(copies) > 0 else 0
    sum += 1 + copy
    count = 0
    for num in win:
        if num in my:
            if count >= len(copies):
                copies.append(0)
            copies[count] += 1 + copy
            count += 1
print(sum)