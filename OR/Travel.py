import random
n = 1
temper = 1000
cRate = 0.999
path = []
F = 0
ans = 0
anspath = []

# Read file
f = open('gr17_d.txt', 'r') #Open file
text = f.readlines() #Read file
f.close() # Close file
table = [text[i].split() for i, val in enumerate(text)] # Create TSB table
#print(table[1][3])

# Create Initial solution
for i, val in enumerate(text):
    path.append(i)

# Calculate Initial solution
for i, val in enumerate(text):
    if i == len(text)-1:
        F = F + int(table[path[i]][path[1]])
    else:
        F = F + int(table[path[i]][path[i+1]])
ans = F
while(1):
    Fn = 0
    # Randomly select 2 place and swap
    x, y = random.sample(path, 2)
    npath = path
    npath[x], npath[y] = npath[y], npath[x]

    # Calculate new solution
    for i, val in enumerate(text):
        if i == len(text)-1:
            Fn = Fn + int(table[path[i]][path[1]])
        else:
            Fn = Fn + int(table[path[i]][path[i+1]])

    # Compare and decide if it is
    if F>Fn:
        path = npath
        F = Fn
        temper = temper*cRate
        ans = Fn
        anspath = npath
    else:
        ran = random.randint(1, 1000)
        if ran < temper:
            path = npath
            F = Fn
            temper = temper*cRate
        else:
            break
print(anspath)
print(ans)