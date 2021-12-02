with open("day 2/input.txt", 'r') as f:
    data = f.readlines()


depth = 0
hori = 0
aim = 0

for i in data:
    i = i.split(' ')
    if i[0] == 'up':
        aim -= int(i[1])
    elif i[0] == 'down':
        aim += int(i[1])
    elif i[0] == 'forward':
        hori += int(i[1])
        depth += int(i[1])*aim

print(depth*hori)