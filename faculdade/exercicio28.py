N= sapos = ratos= coelhos = total= 0

for i in range(int(input(""))):
    quantidadestr, tipo = input('Quantas Cobaias? ').split()
    quantidade= int(quantidadestr)
    tipo = tipo.upper()

    if tipo== "S":
        sapos+= (quantidade)
    elif tipo=="R":
        ratos+= (quantidade)
    elif tipo=="C":
        coelhos+= (quantidade)

total= sapos+ ratos + coelhos

print(f'Total : {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {(coelhos/total)*100:.2f}%')
print(f'Percentual de ratos: {(ratos/total)*100:.2f}%')
print(f'Percentual de sapos: {(sapos/total)*100:.2f}%')