with open("day 3/input.txt", 'r') as f:
    data = f.readlines()

s = ''
data1,data2 = (data[::], data[::])
for i in range(len(data1[0])):
    m = {'0':0,'1':0}
    for j in data1:
        j = j.split('\n')[0]
        m[j[i]] += 1
    max = '0' if m['0'] > m['1'] else '1'
    data1 = [
        dat for dat in data1 if dat[i] == max
    ]
    if len(data1) == 1:
        break
s = data1[0]
sb=''
for i in range(len(data2[0])):
    m = {'0':0,'1':0}
    for j in data2:
        j = j.split('\n')[0]
        m[j[i]] += 1
    max = '0' if m['0'] <= m['1'] else '1'
    data2 = [
        dat for dat in data2 if dat[i] == max
    ]
    if len(data2) == 1:
        break

sb = data2[0][:-1] if data[:-1] == '\n' else data2[0]
print(int((s),2)*int((sb), 2))