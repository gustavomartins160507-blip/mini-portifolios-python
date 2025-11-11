
import random
from time import sleep
import time
lista=['🍎','🍆','🍌']
lista2=[]
ganhou1=['🍆','🍆','🍆']
ganhou2=['🍌','🍌','🍌']
ganhou3=['🍎','🍎','🍎']
print(20*'=-')
texto = 'FORTUNE TIGER'
for t in range(5):
    print(texto, end="\r") 
    time.sleep(0.5)
    print(" " * len(texto), end="\r")
    time.sleep(0.5)
print('FORTUNE TIGER')
print(20*'=-')
dinheiro=float(input('quanto de dinheiro quer colocar? '))
while True:
    for m in range(10): 
        print(lista[random.randint(0,2)],end=' ',flush=True)
        sleep(0.1)
        print(lista[random.randint(0,2)],end=' ',flush=True)
        sleep(0.1)
        print(lista[random.randint(0,2)],flush=True)
        sleep(0.2)
    lista2=[]
    for e in range(3):
        escolha=random.choice(lista)
        lista2.append(escolha)
        print(escolha,end=' ')
    if lista2 == ganhou1:
        print('\nVOCE GANHOU')
        print(f'dinheiro recebido {2*dinheiro}')
    elif lista2 == ganhou2:
        print('\nVOCE GANHOU')
        print(f'dinheiro recebido {2*dinheiro}')
    elif lista2 == ganhou3:
        print('\nVOCE GANHOU')
        print(f'dinheiro recebido {2*dinheiro}')
        break
print('Fim de jogo')