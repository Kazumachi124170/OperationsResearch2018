import random
import time
start_time = time.time()
n = 1000
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
while n > 0:
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
    # Compare and decide if continute
    if F>Fn:
        path = npath
        F = Fn
        temper = temper*cRate
        if ans>Fn:
            ans = Fn
            anspath = npath
    else:
        ran = random.randint(1, 1000)
        if ran < temper:
            path = npath
            F = Fn
            temper = temper*cRate
    n = n-1
anspath.append(anspath[0])
print('The approximate optimal path is: ', anspath)
print('The approximate optimal solution is: ', ans)
print('Running time is: ', time.time()-start_time, '(sec)')