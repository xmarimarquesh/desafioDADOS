from itertools import product

# Lista de caracteres disponíveis
caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Gera todas as combinações possíveis com 6 posições
combinacoes = list(product(caracteres, repeat=6))

# Exibe as primeiras 5 combinações para verificar o resultado
c = 1;
for combinacao in combinacoes[:100]:
    print(c, " : ", combinacao)
    c+=1
