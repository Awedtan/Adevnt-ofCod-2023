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
        
        self.val = int(self.val)

    def get(i, j):
        if f"{i},{j}" in Part.parts:
            return Part.parts[f"{i},{j}"]
        else:
            return False

class Gear:
    gears = []
    def __init__(self, i, j):
        Gear.gears.append(self)
        self.parts = []
        if Part.get(i-1, j-1) and not Part.get(i-1, j-1).counted:
            self.parts.append(Part.get(i-1, j-1))
            Part.get(i-1, j-1).counted = True
        if Part.get(i-1, j) and not Part.get(i-1, j).counted:
            Part.get(i-1, j).counted = True
            self.parts.append(Part.get(i-1, j))
        if Part.get(i-1, j+1) and not Part.get(i-1, j+1).counted:
            Part.get(i-1, j+1).counted = True
            self.parts.append(Part.get(i-1, j+1))
        if Part.get(i, j-1) and not Part.get(i, j-1).counted:
            Part.get(i, j-1).counted = True
            self.parts.append(Part.get(i, j-1))
        if Part.get(i, j+1) and not Part.get(i, j+1).counted:
            Part.get(i, j+1).counted = True
            self.parts.append(Part.get(i, j+1))
        if Part.get(i+1, j-1) and not Part.get(i+1, j-1).counted:
            Part.get(i+1, j-1).counted = True
            self.parts.append(Part.get(i+1, j-1))
        if Part.get(i+1, j) and not Part.get(i+1, j).counted:
            Part.get(i+1, j).counted = True
            self.parts.append(Part.get(i+1, j))
        if Part.get(i+1, j+1) and not Part.get(i+1, j+1).counted:
            Part.get(i+1, j+1).counted = True
            self.parts.append(Part.get(i+1, j+1))

while True:
    line = input()
    if line =='':
        break
    arr.append([])
    for char in line:
        arr[i].append(char)
    i+=1

for i, row in enumerate(arr):
    for j, char in enumerate(row):
        if char.isdigit():
            Part(i, j)

for i, row in enumerate(arr):
    for j, char in enumerate(row):
        if char == '*':
            Gear(i, j)

sum = 0
for gear in Gear.gears:
    if len(gear.parts) == 2:
        sum += gear.parts[0].val * gear.parts[1].val
print(sum)