i= 1
j= 60

print(f'I={i} J={j}')
for i in range(20):
    i+=3
    j-=5
    print(f'I={i} J={j}')

    if j==0:
        break