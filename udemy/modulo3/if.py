idade = input('qual sua idade? ') # me retorna uma string

if idade.isnumeric() is False:
    print('porfavor digite um numeri')
    exit() # sai do programa

int_idade = int(idade)

if int_idade >= 18:
    print('voce e maior de idade')
    
else:
    print('voce e menor de idade')