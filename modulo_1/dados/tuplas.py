
# TUPLAS
#==================================================

# Astuplassãoestruturasdedadosordenadasdotipotupleesão
# semelhantesàslistas,comumadiferençafundamental:tuplassão
# imutáveis.

# Criação de uma tupla homogênea
tupla = (0, 1, 2, 3, 4)
print(tupla)
# Tupla heterogênea
tupla2 = (2, 'a', 5.44, True, None)
print(tupla2)
# Tupla vazia
tupla3 = ()
print(tupla3)
# acesso por índices
print(tupla[0])
print(tupla[3])
print(tupla[-1])
# acesso por slices
print(tupla2[1:4])
print(tupla2[-2:])
print(tupla2[:])


t1 = (30, 10, 20)
t2 = (2, 'a', 5.44, True)
# Operações de concatenação (+), repetição (*) e filiação (in)
print(t1 + t2)
print(t1 * 3)
print(10 in t1)
# Funções úteis
print(len(t2)) # len: retorna a quantidade de elementos da tupla
print(min(t1)) # min: retorna o menor elemento da tupla
print(max(t1)) # max: retorna o maior elemento da tupla
print(sum(t1)) # sum: retorna a soma dos elementos da tupla
# Métodos que retornam valores
print(t1.index(20)) # index: retorna o índice da primeira ocorrência do elemento
print(t2.count('a')) # count: conta as ocorrências do elemento