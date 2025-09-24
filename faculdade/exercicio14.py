tempoS= int(input("Qual o tempo do evento em segundos? "))

horas= tempoS//3600
tempoS= tempoS%3600
minutos= tempoS//60
tempoS= tempoS%60

print(f'{horas}:{minutos}:{tempoS}')