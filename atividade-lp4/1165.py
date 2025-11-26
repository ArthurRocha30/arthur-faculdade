N= int(input())

for i in range(N+1):
    x=int(input())
    divisor= 2
    primo= True
    if x<=1:
        primo=False
    else:

        while divisor<x:
            if x%divisor==0:
                primo=False
                break
            divisor+=1
    if primo:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
    
