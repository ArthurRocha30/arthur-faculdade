peso= float(input('Qual o peso do peixe? '))
excesso= peso-50

print(f'O peso do peixe é de {peso:.2f}Kg')
if excesso>0:
    multa= excesso*4
    print(f'O excesso é de {excesso:.2f}Kg')
    if excesso>1:
        print(f'A multa é de R${multa:.2f}')
    elif excesso>=1:
        print(f"A multa é de R${multa:.2f}")
else:
    print('O peso está dentro do limite, não haverá tributação de multa.')
