lista=list()
contador=0                        
media=0
soma=0
maior=0
while True:
    pessoas=dict()
    pessoas['nome']=str(input('nome: '))
    contador+=1
    pessoas['sexo']=str(input('sexo[M/F]: ')).upper().strip()[0]
    if pessoas['sexo'] =='F':
        pessoas['sexo']='mulher'
    elif pessoas['sexo']=='M':
        pessoas['sexo']='homem'    
    pessoas['idade']=int(input('idade: '))
    pessoas['total']=contador
    soma+=pessoas['idade']
    media=((soma)/contador)
    pessoas['media']=media
    resposta=str(input('que continuar? ')).upper().strip()[0]
    lista.append(pessoas.copy())
    while resposta != 'N' and resposta !='S':
        print('variavel invalida...')
        print('digite novamente')
        resposta=str(input('que continuar? ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'ao todo tivemos {pessoas["total"]} cadastradas. ')
print(f'a media de idade é {pessoas["media"]} anos.')
mulheres=[p['nome'] for p in lista if p['sexo'] == 'mulher']
if mulheres:
    print(f'as mulheres cadastradas foram {",".join(mulheres)}')
else:
    print(f'nao tivemos mulheres cadastradas...')
print('=-=- segue a lista com as pessoas com a idade acima de 40 anos=-=-')
for p in lista:
    if p['idade']>=40:
        print(f'nome: {p["nome"]}, sexo: {p["sexo"]},idade: {p["idade"]}')
print('programa encerrado...')
