val = 0
while True:
    arr = []
    line = input()
    if line == '':
        break
    for char in line:
        if char.isdigit():
            arr.append(char)
    val += 10*int(arr[0]) + int(arr[len(arr)-1])
print(val)