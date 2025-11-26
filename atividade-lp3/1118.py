
calculo=1
while calculo == 1:

    n1 = float(input())
    while n1 < 0 or n1 > 10:
        print("nota invalida")
        n1 = float(input())

    n2 = float(input())
    while n2 < 0 or n2 > 10:
        print("nota invalida")
        n2 = float(input())

    
    media= (n1+n2)/2
    print(f"media = {media:.2f}")
    calculo= int(input("novo calculo (1-sim 2-nao): "))
    
    while calculo<1 or calculo>2:
        calculo= int(input("novo calculo (1-sim 2-nao): "))



    