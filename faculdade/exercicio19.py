N1,N2,N3,N4= map(float,input().split(' '))

media= ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

print(f'Media: {media:.1f}')
if media>=7.0:
    print('Aluno aprovado.')
elif media<5.0:
    print('Aluno Reprovado.')
elif 5.0<= media <=6.9:
    print('Aluno em exame.')
    exame= float(input("Digite a nota do exame: "))
    print(f'Nota do exame: {exame:.1f}')
    notafinal= (exame+media)/2

    if notafinal>=5.0:
        print('Aluno aprovado.')
        print(f'Media final: {notafinal:.1f}')
    elif notafinal<5.0:
        print('Aluno reprovado.')
        print(f'Media final: {notafinal:.1f}')

