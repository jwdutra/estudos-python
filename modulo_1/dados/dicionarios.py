

# Asoutrasestruturasdedadosquevimosatéomomentosão
# formadasporcoleçõesdeitens,ordenadasounão.EmPython,um
# dicionário,queédotipodedadosdict,tambéméumacoleçãodeitens,
# entretantocadaelementoéumparkey–value(chave–valor).Estespares
# indicamquecadaelementopossuíumvalor/valueatreladoàuma
# chave/key


# Dicionário onde as chaves são do tipo string
d1 = {'nome': 'Antônio', 'idade': 36, 'sexo': 'masculino'}
print(d1)
# Dicionário onde as chaves são do tipo inteiro
d2 = {2: 'dois', 1: 'um', 4: 'quatro', 3: 'três', 0: 'zero'}
print(d2)
# Dicionário com chaves de tipos mistos
d3 = {2: 'a', 5.44: True, 'key': None}
print(d3)
# Dicionário vazio
d4 = {}
print(d4)



# Criação dos dicionários
d1 = {2: 'dois', 1: 'um', 4: 'quatro', 3: 'três', 0: 'zero'}
d2 = {'nome': 'Antônio', 'idade': 36, 'sexo': 'masculino'}
# Acesso aos elementos
print(d1[0])
print(d1[2])
print(f'Meu nome é {d2["nome"]} e tenho {d2["idade"]} anos')


# Criação do dicionário
d1 = {'nome': 'Antônio', 'idade': 36, 'sexo': 'masculino'}
# Acesso por meio do operador []
print(d1['nome'])

# Acesso por meio do método get()
print(d1.get('idade'))

# Atualização do valor da chave 'nome'
d1['nome'] = 'Antônio Carlos'
print(d1)
# Adição da chave 'endereço'
d1['endereço'] = 'Rua 123'
print(d1)


# Cria o dicionário
d1 = {'zero': 0, 'um': 1, 'dois': 2, 'três': 3, 'quatro': 4}
print(d1)
# Encontra a maior e menor chave
print('Maior e menor chave:', max(d1), min(d1))
# Adiciona elementos de um outro dicionario
d1.update({'cinco': 5, 'seis': 6})
print(d1)
# Verifica se o dicionário possui as seguintes chaves
print("A chave 'dois' está no dicionário?", 'dois' in d1)
print("A chave 'cinco' não está no dicionário?", 'dois' in d1)
# Remove o elemento com chave 'zero'
d1.pop('zero')
print(d1)


# Cria o dicionário
d1 = {'zero': 0, 'um': 1, 'dois': 2, 'três': 3, 'quatro': 4}
# Itera sobre as chaves
for key in d1:
    if key == 'três':
        print('Chave três encontrada!')
for key in d1.keys():
    if key == 'dez':
        print('Chave quatro encontrada!')
# Itera sobre os valores
soma = 0
for value in d1.values():
    soma = soma + value
    print('Soma dos valores do dicionário:', soma)
# Itera sobre os itens
for key, value in d1.items():
    print(key, value)