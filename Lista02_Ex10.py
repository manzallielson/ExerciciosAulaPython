'''
Escreva um programa  que conte o número de vogais presentes em uma
string informada via teclado por um usuário.
Observação: as letras podem estar grafadas em caixa alta ou caixa baixa. 
'''

def contarVogais(frase):
    qtdVogais = 0
    
    for carac in frase:
        if carac in 'aAeEiIoOuU':
            qtdVogais += 1

    return qtdVogais

# Início do Programa

frase = input('Digite uma frase: ')

print('Qtd Vogais = ', contarVogais(frase))




