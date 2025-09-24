valortotal= int(input("Qual o valor total? "))

print(valortotal)

notas= [100,50,20,10,5,2,1]

for nota in notas:
    quantidade= valortotal// nota
    print(f'{quantidade} nota(s) de R$ {nota},00')
    valortotal= valortotal% nota
