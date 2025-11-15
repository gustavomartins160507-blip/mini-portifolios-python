from random import randint
somatorio=0
resultado=0
while True:
    computador=(randint(1,10))
    escolha=int(input('escolha um numero de 1 a 10: '))
    if escolha > 10:
        print('escolha maior de 10, faça de novo...')
        continue
    imparpar=str(input('impar ou par: ')).upper().strip()
    if imparpar != 'IMPAR' and imparpar!= 'PAR':
        print('escolha invalida...')
        break
    somatorio=computador+escolha
    if somatorio % 2 == 0:
        resultado='PAR'
    else:
        resultado='IMPAR'
    if resultado == imparpar:
        print('Você ganhou...')
        continuar=str(input('quer continuar? ')).upper().strip()[0]
        if continuar != 'S':
            print('Fim de jogo...')
            break
    else:
        print('Você perdeu...')
        print(f'computador escolheu {computador}...')
        break
    