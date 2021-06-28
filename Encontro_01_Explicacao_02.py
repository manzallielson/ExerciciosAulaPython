# CONCATENANDO DADOS NA SAÍDA PADRÃO COM ,

idade = int(input('Digite sua idade: '))

print(type(idade))

print('Pedro tem', idade, 'anos')

# CONCATENANDO DADOS NA SAÍDA PADRÃO COM +

print(type(idade))

print('Pedro tem '+ str(idade) + ' anos')

mensagem = 'Pedro tem '+ str(idade) + ' anos'

print(mensagem)

# EXIBIÇÃO DE DADOS USANDO MÁSCARAS

nome = input('Qual é o seu nome? ')

print('%s tem %i anos, %i irmãos, %.2f m de altura' % (nome, idade, 5, 1.5) )










