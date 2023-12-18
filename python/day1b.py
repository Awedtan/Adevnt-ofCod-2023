val = 0
dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four' : 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

while True:
    arr = []
    line = input()
    if line == '':
        break
    for i in range(len(line)):
        char = line[i]
        if char.isdigit():
            arr.append(char)
        else:
            for j in range(2,6):
                chunk = line[i:i+j]
                if chunk in dict:
                    arr.append(dict[chunk])
    val += 10*int(arr[0]) + int(arr[len(arr)-1])
print(val)