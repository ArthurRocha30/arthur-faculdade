arquivog= float(input('Qual o tamanho do seu arquivo em Gigabytes? '))
conversaom= arquivog *1024
conversaok= (arquivog*1024)*1024

print(f'O arquivo em Megabytes tem tamanho de {conversaom:.2f}MBs')
print(f'O arquivo em Kilobytes tem tamanho de {conversaok:.2f}KBs')