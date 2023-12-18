f = open('input.txt', 'r')

lines = [[line.split()[0], line.split()[1]] for line in f]

# 5, 4, house, 3, 22, 2, high
# 7  6  5      4  3   2  1
def sort(x, y):
    hands = [x[0], y[0]]
    dicts = [{}, {}]

    for i in range(2):
        for hand in hands[i]:
            for char in hand:
                dicts[i][char] = dicts[i][char] + 1 if char in dicts[i] else 1
    
    