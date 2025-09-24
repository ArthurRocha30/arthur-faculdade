N= int(input())

numin= []
numout= []

for i in range(N):
    X= int(input())
    if 10>= X<=20:
        numin.append(X)
    else:
        numout.append(X)

print(f'{len(numin)} in')
print(f'{len(numout)} out')