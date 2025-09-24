def contagem_regressiva(numero):
    while True:
        print(numero)
        numero-=1
        if numero < 0:
            break

contagem_regressiva(200)