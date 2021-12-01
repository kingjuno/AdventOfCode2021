cn=0
with open('input.txt', 'r') as f:
    input_data = [int(num) for num in f.readlines()]
for i in range(0,len(input_data)-3):
    sum1 = input_data[i+2] + input_data[i] + input_data[i+1]
    sum2 = input_data[i+1] + input_data[i+2] + input_data[i+3]
    if sum2 > sum1:
        cn+=1
print(cn)