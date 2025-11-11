from random import randint
def sorteio(lista):
    contador=0
    for c in range(0,5):
        lista.append(randint(1,10))
    for valor in lista:
        if valor % 2 == 0:
            contador+=1
            print(f'os valores pares sao {valor}')
    print(f'temos no total {contador} valores...')
numeros=list()
sorteio(numeros)
print(numeros)