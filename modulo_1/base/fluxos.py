# Condicional

# Exemplo em que a condição é verdadeira
idade = 35
if idade >= 18:
    print('Idade suficiente para CNH!')
    
# Verifica se uma pessoa está apta para se aposentar
idade = 70
tempo_contrib = 20
if idade >= 65 or tempo_contrib >= 35:
    print('Habilitado para solicitar aposentadoria!')
    
# Exemplo em que a condição é verdadeira
idade = 35
if idade >= 18:
    print('Idade suficiente para CNH!')
else:
    print('Idade não suficiente para CNH!')
    
    # Verifica se uma pessoa está apta para se aposentar
idade = 20
tempo_contrib = 20
if idade >= 65 or tempo_contrib >= 35:
    print('Habilitado para solicitar aposentadoria!')
else:
    print('Não habilitado para solicitar aposentadoria!')
    
# Verifica se uma pessoa está apta para se aposentar
idade = 20
tempo_contrib = 20
if idade >= 65:
    print('Habilitado para aposentadoria por idade!')
else:
    if tempo_contrib >= 35:
        print('Habilitado para aposentadoria por tempo de contribuição!')
    else:
        print('Não habilitado para solicitar aposentadoria!')    
        
        
# idade 22 anos, faixa etária: Adulto
idade = 22
if idade < 12:
    faixa_etaria = 'Criança'
elif idade < 18:
    faixa_etaria = 'Adolescente'
elif idade < 60:
    faixa_etaria = 'Adulto'
else:
    faixa_etaria = 'Idoso'
print('Faixa Etária: ', faixa_etaria)        



# Estruturas de repetição

# exemplo com n = 15
n = 15
soma = 0
contador = 0
while contador <= n:
    soma = soma + contador
    contador = contador + 1
print(f'A soma dos primeiros {n} inteiros é {soma}')


# exemplo de palavra: araraquara
p = 'araraquara'
contador = 0
for letra in p:
    if letra == 'a':
        contador = contador + 1
print(f"A palavara {p} possuí {contador} letras 'a'")

# exemplo com n = 15
n = 15
soma = 0
for num in range(n + 1):
    soma = soma + num
print(f'A soma dos primeiros {n} inteiros é {soma}')


# Realiza a busca na faixa de 250 e 300
for num in range(250, 301):
    # verifica se o número é divisível por 21
    if num % 21 == 0:
        print('Número encontrado:', num)
    # se for divísivel por 21, interrompe a busca
    break