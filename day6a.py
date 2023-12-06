f = open('input.txt', 'r')
times = [int(x) for x in f.readline().split() if x.isdigit()]
dists = [int(x) for x in f.readline().split() if x.isdigit()]

result = 1
for i,time in enumerate(times):
    count = 0
    for j in range(time):
        if j * (time-j) > dists[i]:
            count += 1
    result *= count
print(result)