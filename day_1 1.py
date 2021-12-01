cn=0
with open('input.txt', 'r') as f:
    input_data = [int(num) for num in f.readlines()]
for i in range(0,len(input_data)-1):
    if input_data[i] < input_data[i+1]:
        cn+=1
print(cn)