positivos= []

for i in range(1,7):
    valor= float(input())
    if valor>0:
        positivos.append(valor)
    
print(f"{len(positivos)} valores positivos")
print(f"{sum(positivos)/len(positivos):.1f}")
