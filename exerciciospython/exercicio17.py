from math import ceil

metros= float(input('Indique a área em metros quadrados: '))

PRODUTOS= {
    "lata": {"cap": 18, "preco": 80.00},
    "galao": {"cap": 3.6, "preco": 25.0},
}

def litros(metros, cobertura=6.0, folga=0.10):
    return metros/cobertura*(1+folga)

def apenas_latas(L):
    n= ceil(L/PRODUTOS["lata"]["cap"])
    return n, n*PRODUTOS["lata"]["preco"]