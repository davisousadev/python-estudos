nome = input('Digite seu nome: ')

if nome.isdigit():
    print('digite uma letra')
else:
    quantidade_de_caracteres = len(nome)
    if quantidade_de_caracteres <= 0 or quantidade_de_caracteres <= 2:
        print('digite um nome')
        exit()
    
    if quantidade_de_caracteres == 3:
        print('seu nome e curto')
    elif quantidade_de_caracteres <= 5 or quantidade_de_caracteres <= 6:
        print('seu nome tem um tamanho nomral')
    else:
        print('seu nome e muito grande')
