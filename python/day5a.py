line = input()
seeds = [int(x.strip()) for x in line.split() if x.isdigit()]
ssmap = []
sfmap = []
fwmap = []
wlmap = []
ltmap = []
thmap = []
hlmap = []

while True:
    line = input()
    if line == 'done':
        break

    if line == 'seed-to-soil map:':
        while True:
            line = input()
            if line == '':
                break
            ssmap.append([int(x) for x in line.split()])
    
    if line == 'soil-to-fertilizer map:':
        while True:
            line = input()
            if line == '':
                break
            sfmap.append([int(x) for x in line.split()])

    if line == 'fertilizer-to-water map:':
        while True:
            line = input()
            if line == '':
                break
            fwmap.append([int(x) for x in line.split()])

    if line == 'water-to-light map:':
        while True:
            line = input()
            if line == '':
                break
            wlmap.append([int(x) for x in line.split()])

    if line == 'light-to-temperature map:':
        while True:
            line = input()
            if line == '':
                break
            ltmap.append([int(x) for x in line.split()])

    if line == 'temperature-to-humidity map:':
        while True:
            line = input()
            if line == '':
                break
            thmap.append([int(x) for x in line.split()])

    if line == 'humidity-to-location map:':
        while True:
            line = input()
            if line == '':
                break
            hlmap.append([int(x) for x in line.split()])

def get(map, i):
    for list in map:
        if i in range(list[1], list[1] + list[2]):
            return i - list[1] + list[0]
    return i

min = 999999999999
for seed in seeds:
    location = get(hlmap, get(thmap, get(ltmap, get(wlmap, get(fwmap, get(sfmap, get(ssmap, seed)))))))
    min = location if location < min else min
print(min)