horario = input('que horas são? ')
if horario.isdigit():
    horario_int = int(horario)
    if horario_int >= 0  and horario_int <= 11:
        print('bom dia')
        exit()
    if horario_int >= 12  and horario_int <= 17:
        print('boa tarde')
        exit()
    if horario_int >= 18  and horario_int <= 23:
        print('boa noite')
        exit()
else:
    print('digite um numero inteiro')