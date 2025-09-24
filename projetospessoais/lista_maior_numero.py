def maior_numero(lista_numero):
    maior_numero = lista_numero[0]
    for numero in lista_numero:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

lista = [4,5,6,10,12]
maior_numero_lista= maior_numero(lista)

print(f"O maior número da lista é {maior_numero_lista}")