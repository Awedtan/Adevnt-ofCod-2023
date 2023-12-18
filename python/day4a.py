sum=0
while True:
    line = input()
    if line == '':
        break

    line = line[line.index(':')+1:].split('|')
    win = [num for num in line[0].strip().split()]
    my = [num for num in line[1].strip().split()]

    card=0
    for num in win:
        if num in my:
            card = 1 if card == 0 else card*2
    sum+=card
print(sum)