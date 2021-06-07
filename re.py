from tqdm import tqdm
from time import sleep
while True:
    valores = []
    cont = 0
    while True:
        valores.append(str(input('Nome do produto: ')))
        valores.append(float(input('Valor do produto:')))
        cont += 1
        # ---------sim ou nao---------
        q = str(input('Quer registrar mais algum? [S/N]')).strip().upper()

        if q == 'N':
            break
    # ---------conclusao---------
    print('\n ' * 2)
    print('=' * 40)
    print(' ' * 10, 'Tacabela de valores')
    print('=' * 40)
    for i in valores:
        if type(i) is str:
            print(f'{i:.<32}', end='')
        else:
            print(f'R$ {i:>5.2f}')
    print('\n ' * 1)
    print(f'✍ Voce registrou {cont} item a venda. ✔ !!!')
    print('=' * 40)
    print('\n '*2)
    valores2 = valores [:]
    q2 = str(input('Quer registrar mais alguma coisa? [S/N]')).strip().upper()
    if q2 == 'N':
        break
    else:   
        #--------- continuar de listagem apartir da lsita antiga---------
        valores2 = []
        c = 0
        while True:
            valores.append(str(input('Nome do produto: ')))
            valores.append(float(input('Valor do produto:')))
            c += 1

            # sim ou nao
            q = str(input('Quer registrar mais algum? [S/N]')).strip().upper()

            if q == 'N':
                break
        # conclusao
        print('\n ' * 2)
        print('=' * 40)
        print(' ' * 10, 'Tacabela de valores')
        print('=' * 40)
        for i in valores:
            if type(i) is str:
                print(f'{i:.<32}', end='')
            else:
                print(f'R$ {i:>5.2f}')
        print('\n ' * 1)
        print('-'*40)
        print(f'✍ Voce registrou mais {c} item a venda. ✔ !!!')
        print(f'Total de itens registrado: {c+cont} ✔✔')
        print('=' * 40)
        #---------fim---------
        q = str(input('Salvar:  [S/N]')).strip().upper()
        if q == 'S':
            break
#---------carregamento---------            
for i in tqdm(range(100)):
    ...
    sleep(0.02)
print('Salvo com exito!')

