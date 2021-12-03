with open("day 3/input.txt", 'r') as f:
    data = f.readlines()

s = ''

for i in range(len(data[0])-1):
    m = {'0':0,'1':0}
    for j in data:
        j = j.split('\n')[0]
        m[j[i]] += 1
    if m['0'] > m['1']:
        s+='0'
    else:
        s+='1'
sb = ''
for i in s:
    if i == '0':
        sb+='1'
    else:
        sb+='0'

print(int((s),2)*int((sb), 2))
