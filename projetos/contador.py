from time import sleep
def l():
    print('=-'*20)
def contador(i,f,p):
    if p<0:
        p*=-1
    if p==0:
        p=1
    l()
    print(f'Contagem de {i} até {f} indo de {p} em {p}')
    if i < f:
        cont=i
    while cont<=f:
        cont+=p
        print(f'{cont}',end=' ',flush=True)
        sleep(0.5)
    else:
        cont=i
        while cont >=f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont-=p
    print('FIM')
contador(1,10,1)
contador(1,10,2)
inicio=int(input('INICIO: '))
fim=int(input('FIM: '))
passo=int(input('PASSO: '))
contador(inicio,fim,passo)