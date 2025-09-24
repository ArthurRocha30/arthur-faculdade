valor = float(input())

notas= [100,50,20,10,5,2]

moedas= [1.0,0.50,0.25,0.10,0.05,0.01]

print('NOTAS:')
for nota in notas:
    quantidadenotas= valor//nota 
    print(f'{quantidadenotas} nota(s) de R$ {nota}.00')
    valor= valor% nota

print('MOEDAS: ')

for moeda in moedas:
    quantidademoedas = valor// moeda
    print(f'{quantidademoedas:.0f} moeda(s) de R$ {moeda:.2f}')
    valor= valor%moeda
    