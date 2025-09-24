par= []

for i in range(5):
    num= int(input())
    if num%2==0:
        par.append(num)
    
print(f'{len(par)} valores pares')