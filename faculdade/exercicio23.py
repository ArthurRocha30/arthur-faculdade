A,B,C= sorted(map(int,input().split(' ')), reverse=True)

if A>=B+C:
    print('NAO FORMA TRIANGULO')
if A**2==B**2+C**2:
    print('TRIANGULO RETANGULO')
if A**2>B**2+C**2:
    print('TRIANGULO OBTUSANGULO')
if A**2<B**2+C**2:
    print('TRIANGULO ACUTANGULO')
if A==B==C:
    print('TRIANGULO EQUILATERO')
if A==B or A==C or B==C:
    print('TRIANGULO ISOSCELES')