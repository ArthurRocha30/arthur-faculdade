x= int(input())
y= int(input())

menor=x
maior=y

if x<y:
    maior=y
    menor=x
if y<x:
    maior=x
    menor=y

soma = 0
atual= menor
while atual<= maior:
    soma += atual * (atual % 13 !=0)
    atual += 1

print(soma)