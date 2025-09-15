# o numero digitado pelo user vem como str
numero = input("Digite um numero inteiro: ")

# verificando se o numero e um numero mesmo entrae 0 a 9
if numero.isdigit():
    # convertendo o numero de str para int
    if int(numero) % 2 == 0:
        print("O numero é par.")
    else:
        print("O numero é ímpar.")
else:
    print("Isso não é um numero inteiro.")