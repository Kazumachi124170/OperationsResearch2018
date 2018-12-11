import random
import time
import math

start_time = time.time()
n = 100 # Maximum iteration time
temper = 100 # Temperature
cRate = 0.99 # Cooling rate
path = []
F = 0
ans = 0
anspath = []

# Read file
f = open('gr17_d.txt', 'r') #Open file
text = f.readlines() #Read file
f.close() # Close file
table = [text[i].split() for i, val in enumerate(text)] # Create TSB table

# Create Initial solution
for i, val in enumerate(text):
    path.append(i)

# Calculate Initial solution
for i, val in enumerate(text):
    if i == len(text)-1:
        F = F + int(table[path[i]][path[0]])
    else:
        F = F + int(table[path[i]][path[i+1]])
ans = F

# Trail-and-error
while n > 0:
    Fn = 0
    # Randomly select 2 place and swap
    x, y = random.sample(path, 2)
    npath = path
    npath[x], npath[y] = npath[y], npath[x]
    # Calculate new solution
    for i, val in enumerate(text):
        if i == len(text)-1:
            Fn = Fn + int(table[path[i]][path[0]])
        else:
            Fn = Fn + int(table[path[i]][path[i+1]])
    # Compare and decide if continute
    if F>Fn:
        # New path is shorter
        path = npath
        F = Fn
        if ans>Fn:
            ans = Fn
            anspath = npath
    else:
        # New path is longer
        ran = random.random()
        if ran <= math.exp(-(Fn-F)/temper):
            path = npath
            F = Fn
        else:
            continue
    temper = temper*cRate
    n = n-1
    print(n)
    print(temper)
anspath.append(anspath[0])
print('The approximate optimal solution is: ', anspath)
print('The fitness funcion value is: ', ans)
print('Running time is: ', time.time()-start_time, '(sec)')