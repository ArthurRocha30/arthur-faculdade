valor= float(input())

#sem taxa
if valor<= 2000.00:
    print('Isento')
#taxa máxima
elif valor > 4500.00:
    taxa3= valor-4500.00
    imposto1= 1000.00*0.08
    imposto2= 1500.00*0.18
    imposto3= taxa3*0.28
    print(f'R$ {imposto1+imposto2+imposto3:.2f}')
#taxa media
elif valor >= 3001.00 and valor <= 4500.00:
    taxa2= valor-3000.00
    imposto1= 1000.00*0.08
    imposto2= taxa2*0.18

    print(f'R$ {imposto1+imposto2:.2f}')
#taxa minima
else:
    taxa1=valor-2000.00
    imposto1= taxa1*0.08
    print(f'R$ {imposto1:.2f}')