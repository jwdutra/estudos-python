nome = "Walter"
print('Ola', nome, 'Com vai?')


# define o valor do limiar
limiar = 5

menores = [] # cria lista menores
maiores = [] # cria lista maiores

# divide os números de 1 a 10 em maiores e menores
for i in range(10): 
    if (i < limiar):
        menores.append(i)
    elif (i > limiar):
        maiores.append(i)

# imprime na tela os valores das listas
print('Resultado final')
print('menores:', menores)
print('maiores:', maiores)

# utilização de uma variável inexistente (não definida)


x = 10
print(type(x))

x = 10
y = 4
z = 4.5
print('x + y + z=', x + y + z)
print('x - 3 =', x - 3)
print('x * z =', x * z)
print('x * 2 =', x * 2)
print('x / (y + 2) =', x / (y + 2))
print('x % y =', x % y)
print('x // y =', x // y)
print('x ** z =', x ** z)

# P Parênteses
# E Exponenciação
# M Multiplicação
# D Divisão
# A Adição
# S Subtração

palavra = 'consolação'
# consola
print(palavra[:7])
# sol
print(palavra[3:6])
# sola
print(palavra[3:7])
# ação
print(palavra[-4:])
# palavra original
print(palavra[:])


s1 = 'consolação'
s2 = 'sola'
print(s1 in s2)
print(s2 in s1)
print('solar' in s1)
print('solar' not in s2)

s1 = 'Belo Horizonte'
s2 = 'Esta é uma frase, com uma vírgula.'
print(s1.upper()) # todas as letras maiúsculas
print(s1.lower()) # todas as letras minúsculas
print(s2.title()) # primeira letra de cada palavra em maísculo
print(s1.replace('Horizonte', 'Monte')) # substitui 'Horizonte' por 'Monte'
print(s1.startswith('Belo')) # verifica se a string começa com 'Belo'
print(s1.endswith('Monte')) # verifica se a string termina com 'Monte'
print(s2.find('frase')) # retorna o índice da primeira ocorrência da palavra frase
print(s2.split()) # particiona a string em outras, que são separadas por um espaço
print(s2.split(',')) # particiona a string em outras, que são separadas por ','
s3 = '    palavra com espaços    '
print(s3.strip()) # remove os espaços extras no início e fim da string


print('nome'.upper())
print('a, b, c, d'.split(','))
print('Belo Horizonte'.replace('Horizonte', 'Monte'))


# Formartação de strings

nascimento = 1986
ano_atual = 2022
idade = ano_atual - nascimento
print(f'Eu tenho {idade} anos')

nascimento = 1986
ano_atual = 2022
print(f'Eu tenho {ano_atual - nascimento} anos')

palavra = 'consolação'
print(f'A palavra {palavra.upper()} possuí {len(palavra)} letras')

orcamento = 5000
vlr_gasto = 430
pct = (vlr_gasto/orcamento) * 100
print(f'Porcentagem já gasta do orçamento: {pct}%')

orcamento = 5000
vlr_gasto = 430
pct = (vlr_gasto/orcamento) * 100
print(f'Porcentagem já gasta do orçamento: {pct:.2f}%')

orcamento = 5000
vlr_gasto = 430
pct = (vlr_gasto/orcamento)
print(f'Porcentagem já gasta do orçamento: {pct:.2%}')