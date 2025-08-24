valor_1 = input('digite um valor: ')
valor_2 = input('digite outro valor: ')

if valor_1 == valor_2:
    print('os valores sao iguais')
    exit()

if valor_1 > valor_2:
    print(f'o valor {valor_1} e maior que o valor {valor_2}')
else:
    print(f'o valor {valor_2} e maior que o valor {valor_1}')