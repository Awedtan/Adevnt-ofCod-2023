f = open('input.txt', 'r')
time = int(''.join([x for x in f.readline().split() if x.isdigit()]))
dist = int(''.join([x for x in f.readline().split() if x.isdigit()]))

def search(end, dist):
    start, min = 0, 0
    while start <= end:
        mid = int((start+end)/2)
        middist = mid * (time-mid)
        if middist == dist:
            return mid
        elif middist > dist:
            end = mid-1
            min = mid
        else:
            start = mid+1
    return min

min = search(time/2, dist)
print(time - 2*min + 1)