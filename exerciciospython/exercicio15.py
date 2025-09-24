porhora= float(input("Quanto você ganha por hora? "))
horasmes= int(input('Quantas horas você fez no mês? '))
salariobruto= porhora*horasmes
desconto= (salariobruto*24)/100
inss= (salariobruto*8)/100
sindicato=(salariobruto*5)/100
impostorenda=(salariobruto*11)/100
salarioliquido= salariobruto-desconto

print(f'O seu salário bruto é R$ {salariobruto:.2f}')
print(f'O valor pago de Imposto de Renda é R$ {impostorenda:.2f}')
print(f'O valor pago de INSS é R$ {inss:.2f}')
print(f'O valor pago de sindicato é R$ {sindicato:.2f}')
print(f'O seu salário líquido é R$ {salarioliquido:.2f}')