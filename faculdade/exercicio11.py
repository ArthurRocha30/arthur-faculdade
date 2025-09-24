from math import sqrt 

x1, y1= map(float, input("Indique x1 e y1: ").split(" "))
x2, y2= map(float, input("Indique x2 e y2: ").split(" "))

print(f'{sqrt((x2-x1)**2+(y2-y1)**2):.4f}')