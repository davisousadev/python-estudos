nome_usuario = input('Qual seu nome? ')
idadade_usuario = input('Qual sua idade? ')

if nome_usuario and idadade_usuario:
    print(f'Seu nome é {nome_usuario}')
    print(f'Seu nome invertido é {nome_usuario[::-1]}')
    print(f'Seu nome tem {len(nome_usuario)} letras')
    print(f'A primeira letra do seu nome é {nome_usuario[0]}')
    print(f'A última letra do seu nome é {nome_usuario[-1]}')
    print(f'Sua idade é {idadade_usuario}')
else:
    print('Nome ou idade não fornecidos.')