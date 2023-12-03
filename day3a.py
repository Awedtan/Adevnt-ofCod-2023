arr = []
i = 0

class Part:
    parts = {}
    def __init__(self, i, j):
        self.val = f"{arr[i][j]}"
        self.cells = [[i,j]]
        self.valid = False
        self.counted = False

        for left in range(j-1, -1, -1):
            if arr[i][left].isdigit():
                self.val = f"{arr[i][left]}{self.val}"
                self.cells.append([i,left])
            else:
                break

        for right in range(j+1, len(arr[i])):
            if arr[i][right].isdigit():
                self.val = f"{self.val}{arr[i][right]}"
                self.cells.append([i,right])
            else:
                break

        for cell in self.cells:
            Part.parts.update({f"{cell[0]},{cell[1]}": self})

    def create(i, j):
        # if Part.get(i, j):
            # print(f"{i},{j}")
        Part(i, j)

    def get(i, j):
        if f"{i},{j}" in Part.parts:
            return Part.parts[f"{i},{j}"]
        else:
            return False

while True:
    line = input()
    if line =='':
        break
    arr.append([])
    for char in line:
        arr[i].append(char)
    i+=1

i=0
for row in arr:
    j=0
    for char in row:
        if(char.isdigit()):
            # print(f"Create: {i},{j}: {char}")
            Part.create(i, j)
        j+=1
    i+=1

i=0
j=0
for i in range(len(arr)):
    row = arr[i]
    for j in range(len(row)):
        char = row[j]
        if (not char.isdigit()) and char != '.':
            if Part.get(i-1, j-1):
                Part.get(i-1, j-1).valid = True
            if Part.get(i-1, j):
                Part.get(i-1, j).valid = True
            if Part.get(i-1, j+1):
                Part.get(i-1, j+1).valid = True
            if Part.get(i, j-1):
                Part.get(i, j-1).valid = True
            if Part.get(i, j+1):
                Part.get(i, j+1).valid = True
            if Part.get(i+1, j-1):
                Part.get(i+1, j-1).valid = True
            if Part.get(i+1, j):
                Part.get(i+1, j).valid = True
            if Part.get(i+1, j+1):
                Part.get(i+1, j+1).valid = True

sum = 0
for thing in Part.parts:
    part = Part.parts[thing]
    if part.valid and not part.counted:
        sum += int(part.val)
        part.counted = True
print(sum)