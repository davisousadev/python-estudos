# as f strigs sao forma de formatar texto com variavies 

nome = 'Davi'
idade = 19

apresentacao = f'Ola, meu nome {nome} e eu tenho {idade} anos'
print(apresentacao)

# tbm podemos formatar numeros com suas casas decimais 
altura = 1.70
apresentacao = f'Ola, meu nome {nome} e eu tenho {idade} anos e peso {altura:.2f} kg'
print(apresentacao)