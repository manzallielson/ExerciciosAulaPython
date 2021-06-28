'''
8)  Um valor inteiro positivo n é chamado de quadrado perfeito se existir
uma sequência de ímpares consecutivos a partir do valor 1 cuja soma seja
exatamente igual a n.
Exemplo: para o valor 16 temos 16 = 1 + 3 + 5 + 7.

Assim sendo, 16 é um quadrado perfeito.
Logo, um quadrado perfeito tem a seguinte propriedade: o número de termos
ímpares consecutivos m a partir do valor 1 cuja soma é igual ao quadrado
perfeito corresponde à raiz quadrada do quadrado perfeito.
No exemplo acima, para n=16, o valor de m é 4, o que corresponde à
raiz quadrada de 16.

Faça um programa que solicite ao usuário a digitação de um número.
Este programa deve:
a)	Verificar se valor digitado pelo usuário é um quadrado perfeito.
Se o valor digitado pelo usuário não for um quadrado perfeito,
dê uma mensagem ao usuário.
b)	Se o valor digitado pelo usuário for um quadrado perfeito,
determine o valor de sua raiz quadrada (m) de acordo com o procedimento
descrito acima e imprima na tela. 
'''

n = int(input('Digite um numero: '))
somatorio = 0
i = 1
m = 0

while (somatorio < n):
    somatorio += i
    m+=1 # Contando a qtd de impares

    i+=2

if somatorio==n:
    print('Quadrado Perfeito')
    print('Raiz quadrada = ', m)
else:
    print('NÃO é um quadrado perfeito')

    
