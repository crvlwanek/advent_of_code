with open("input.txt") as file:
    topo = [line.strip() for line in file.readlines()]

directions = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
)

def part1():
    
    total = 0
    for y, row in enumerate(topo):
        for x, char in enumerate(row):

            if char != "0":
                continue

            paths = [(y, x, set())]
            fullTrails = set()
            nines = set()
            rating = 0
            while paths:
                i, j, s = paths.pop(0)
                s.add((i, j))

                if topo[i][j] == "9":
                    nines.add((i, j))
                    fullTrails.update(s)
                    rating += 1
                    continue

                for di, dj in directions:
                    i2, j2 = i + di, j + dj
                    
                    if 0 <= i2 < len(topo) and 0 <= j2 < len(topo[i2]) and int(topo[i][j]) + 1 == int(topo[i2][j2]):
                        paths.append((i2, j2, set(s)))
            
            def printPaths():
                print()
                for i in range(len(topo)):
                    for j in range(len(topo[i])):
                        if (i, j) in fullTrails:
                            print(topo[i][j], end="")
                        else:
                            print(".", end="")
                    print()

            #printPaths()
            #total += len(nines)
            total += rating
            

    
    print(total)


part1()