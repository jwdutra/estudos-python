
# EmPythonosconjuntos(sets)sãoestruturasdedadosdotiposet,
# não-ordenadas,querepresentamumacoleçãodeitensúnicos,ouseja,
# itenssemrepetições.Assimcomoalista,oconjuntotambéméuma
# estruturamutável,suportandooperaçõesdeinserção,alteraçãoeremoção
# de elementos.

# Criação de um conjunto homogêneo
c1 = {3, 0, 1, 4, 3}
print(c1)
# Criação do mesmo conjunto, porém com uma ordenação diferente dos itens
c2 = {2, 1, 4, 3, 0}
print(c2)
# Conjunto heterogêneo
c3 = {2, 'a', 5.44, True, None}
print(c3)



# Criação dos conjuntos A e B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print('A:', A)
print('B:', B)
# Operação de União: (A ∪ B)
print('A | B =>', A | B)
print('A.union(B) =>', A.union(B))
# Operação de Interseção: (A ∩ B)
print('A & B =>', A & B)
print('A.intersection(B) =>', A.intersection(B))
# Operação de Diferença: (A - B) e (B - A)
print('A - B =>', A - B)
print('A.difference(B) =>', A.difference(B))
print('B - A =>', B - A)
print('B.difference(A) =>', B.difference(A))



# Criação dos conjuntos A e B
c1 = {1, 2, 3, 4, 5}
c2 = {4, 5}
c3 = {91, 92, 93}
# Adiciona um elemento ao conjunto
c1.add(6)
print(c1)
# Adiciona os elementos de uma sequência iterável
c1.update([2, 4, 6, 8])
print(c1)
# Descarta um elemento do conjunto,
c1.discard(8)
print(c1)
# Diferentemente do set.remove(), o discard não gera um erro
# se o elmento a ser removido não existir
c1.discard(99)
print(c1)
# Verifica se os conjuntos são disjuntos, ou seja,
# se não possuem nenhum elemento em comum
print(c1.isdisjoint(c2))
print(c1.isdisjoint(c3))
# Verifica se o conjunto é subconjunto de outro
print(c1.issubset(c2))
print(c2.issubset(c1))
# Verifica se o conjunto contém outro conjunto (superset)
print(c1.issuperset(c2))
print(c2.issuperset(c1))



# Criação dos conjuntos de alunos das turmas
ING = {'Gabriel', 'Caio', 'Maria', 'Ana', 'Juliano', 'Flávia', 'Rubens', 'Bruna'}
ESP = {'Caio', 'Artur', 'Beatriz', 'Carolina', 'Maria', 'Juliano', 'Bruna', 'Rui'}
FRA = {'Pedro', 'Bruna', 'Paula', 'Tiago', 'Maria', 'Flávia', 'Rui', 'Carolina'}
# Operação de união dos conjuntos (união dos alunos de todas as turmas)
# Também poderia ser: ALL = ING.union(ESP).union(FRA)
ALL = ING | ESP | FRA
# Exibição do resultado
print('Relação de todos os alunos da escola:')
print(ALL)


# 1 – Interseção entre os pares de turmas: (ING & ESP), (ING & FRA) e (ESP & FRA)
# 2 – Calcula a união das interseções
ALUNOS_DESCONTO = (ING & ESP) | (ING & FRA) | (ESP & FRA)
# Exibição do resultado
print('Relação de dos alunos com desconto:')
print(ALUNOS_DESCONTO)


# 1 – Interseção entre os pares de turmas: (ING & ESP), (ING & FRA) e (ESP & FRA)
# 2 – Calcula a união das interseções
ALUNOS_DESCONTO = (ING & ESP) | (ING & FRA) | (ESP & FRA)
# Exibição do resultado
print('Relação de dos alunos com desconto:')
print(ALUNOS_DESCONTO)