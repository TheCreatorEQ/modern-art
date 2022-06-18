import numpy
m = int(input())
n = int(input())
k = int(input())
gold = [0]* n
xgold = [0] * n
ygold = [0] * m
xcount = 0
factor = 0
result = 0
for i in range(k):
    stroke = input().split()
    index = int(stroke[1]) - 1
    if stroke[0] == 'R':
        ygold[index] += 1
    else:
        xgold[index] += 1

count = 0
for i in xgold:
    if i % 2 == 1:
        gold[count] += m
        xcount += 1
    count += 1

for i in ygold:
    if i % 2 == 1:
        gold = list(1+numpy.array(gold))
        factor += xcount*2


    
result = sum(gold) - factor
print(result)
        

