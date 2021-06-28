'''
9)  Faça um programa que valide o dígito de controle de um número de cartão
de crédito que foi passado por parâmetro. Um número de cartão de crédito
consiste em uma sequência de 16 dígitos decimais, sendo o menos significativo
o dígito de controle. Para validar este dígito de controle, processam-se
os dígitos da esquerda para direita, a partir do primeiro até o décimo quinto.
O processamento dos dígitos é feito na forma de um somatório em que os dígitos
em posições pares são somados da forma como aparecem no número do cartão de
crédito e os em posição ímpar são dobrados e depois a soma dos dígitos de
cada valor dobrado é agregada ao somatório.

Uma vez concluído tal cálculo, é computado a diferença entre 10 e o resto da
divisão do somatório por 10. 
Se o valor da diferença assim calculado for igual ao valor do último dígito,
então é altamente provável que o número do cartão de crédito fornecido está
correto e neste caso, o programa deverá informar ao usuário que o cartão é
VÁLIDO. Se tais valores forem distintos, então o número certamente está errado
e o programa deverá informar ao usuário que o cartão é INVÁLIDO. 
Para validar o dígito de controle de um número de cartão de crédito,
solicite ao usuário que digite o número.

Exemplo:
Considere o número de cartão 5231027325131467. Neste caso temos
    somatório = (1 + 0) + 2 + (6) + 1 + (0) + 2 + (1 + 4) + 3 + (4) + 5 + (2) + 3 + (2) + 4 + (1 + 2) = 43
    diferença = 10 - somatório % 10 = 10 - 43 % 10 = 10 - 3 = 7
'''

nro_cartao = int(input('Digite o nro do seu cartao: '))

print(nro_cartao)

# PARTE 01 - separar o digito de controle

dig_controle = nro_cartao % 10
nro_cartao = nro_cartao // 10

print(nro_cartao)

# PARTE 02 - calcular o somatorio

somatorio = 0

for i in range(15, 0, -1):
    ultimo_dig = nro_cartao % 10

    if i%2 != 0: # posição impar
        dobro = ultimo_dig * 2

        if dobro<10:
            somatorio += dobro
        else: 
            somatorio += dobro%10 + dobro//10

    else: # posição par
        somatorio += ultimo_dig

    nro_cartao = nro_cartao // 10

print(somatorio)

# PARTE 03 - calcular a diferença

diferenca = 10 - somatorio % 10

print(diferenca)

if diferenca == dig_controle:
    print('CARTÃO VÁLIDO')
else:
    print('CARTÃO INVÁLIDO')

    
