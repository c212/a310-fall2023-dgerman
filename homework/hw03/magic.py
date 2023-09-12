size = 5

m = {}
m["width"] = size
m["height"] = size

def show(m):
    for row in range(m["height"]):
        for col in range(m["width"]):
            if (row, col) in m:
                print(m[row, col], end=" ")
            else:
                print(0, end=" ")
        print()
    print("-----------------------------------")

row = size-1
col= size//2 # or as dieter suggests int(size/2)
for n in range(1,size*size+1):
    m[row, col] = n
    show(m)
    nurow = (row + 1) % size
    nucol = (col + 1) % size
    if (nurow, nucol) in m:
        row = row -1
        col = col
    else:
        row = nurow
        col = nucol
        

