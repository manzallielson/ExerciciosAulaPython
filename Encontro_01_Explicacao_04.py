
idade = int(input('Digite sua idade:'))

sexo = input('Digite seu sexo (M ou F)')

if idade > 18 and sexo == 'F':
    print('Você está autorizada a entrada')
    print('Cuidado! Não deixe sua bolsa no chão')
elif idade > 18 and sexo == 'M':
    print('Você só pode entrar se pagar!')
elif idade < 18:
    print('Você é menor de idade')
    if sexo == 'F' or sexo == 'f':
        print('Meninha')
    else:
        print('Meninho')

print('fim')
