lista = []

while True:
    opcao = input('[i] inserir, [a] apagar, [l] listar ')

    if opcao == 'i':
        item = input('Digite o item: ')
        lista.append(item)
        print('Item adicionado', item)

    if opcao == 'a':
        indice = input('Digite o índice do item a ser apagado: ')
        try:
            indice = int(indice)
            del lista[indice]
        except ValueError:
            print('Índice deve ser um número inteiro')
            continue
        except IndexError:
            print('Índice fora do intervalo da lista')
            continue
        print('Item apagado')

    if opcao == 'l':
        if len(lista) == 0:
            print('Lista vazia')
        else:
            for i, item in enumerate(lista):
                print(i, item)