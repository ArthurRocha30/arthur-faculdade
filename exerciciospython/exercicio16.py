from math import ceil

metrosquadrados= float(input('Qual o tamanho da área em metros quadrados? '))
litro= metrosquadrados*3
latatinta= ceil(litro/18)
preco= latatinta*80

print(f'Você irá precisar de {latatinta} lata(s) de tinta de 18L e lhe custará R$ {preco:.2f}')