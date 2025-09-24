#horários inicio do evento
dia = int(input().split("Dia")[1].strip())
horas, minutos, segundos= map(int, input().split(' : ')) 
#horários do término do evento
diatermino= int(input().split("Dia")[1].strip())
horater,minutoter,segundoter= map(int, input().split(' : '))

#transforma tudo para segundos
tempoinicial= (dia*24*60*60)+(horas*60*60)+(minutos*60)+(segundos)
tempofinal= (diatermino*24*60*60)+(horater*60*60)+(minutoter*60)+(segundoter)

#calcula a duração
duracao= tempofinal-tempoinicial

#transforma de volta para o respectivo padrão
duracaodia= duracao//86400
duracaohora= duracao%86400//3600
duracaominuto= duracao%3600//60
duracaosegundo=duracao%60

print(f'{duracaodia} dia(s)')
print(f'{duracaohora} hora(s)')
print(f'{duracaominuto} minuto(s)')
print(f'{duracaosegundo} segundo(s)')