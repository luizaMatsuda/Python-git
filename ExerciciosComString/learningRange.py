'''
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
F
FU
FUL
FULA
FULAN
FULANO


funcao range gera uma sequencia de numeros (lista) de itens range(inicio, fim, salto)
range(11) - valores de 0 a 10
range(5,11) - valores de 5 a 10
range(2,50,2) - valores de 2 a 50 saltando de 2 em 2
'''
'''
name = input('Digite o seu nome ')
for letter in range(0, len(name) + 1):
    print(name[:letter])
'''
'''

# Apresentar numeros de 0 a 10

for number in range(0, 11):
    print(number)
'''
'''
# Apresentar as dezenas de de 10 a 100
for number in range(10, 110, 10):
    print(number)
'''

#

