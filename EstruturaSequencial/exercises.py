# 1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
#print('Hello Word')

# 2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
'''
number = input('Digite um numero: ')
print('O numero digitado foi: ', number)
'''

# 3 - Faça um Programa que peça dois números e imprima a soma.
'''
firstNumber = input('Digite um numero para a soma: ')
secondNumber = input('Digite o segundo numero: ')
result = float(firstNumber) + float(secondNumber)

# %s e utilizado para string || %d e utilizado para decimal || %f e utilizado para float
print('O resultado da soma entre %s + %s e %f ' % (firstNumber, secondNumber, result))
'''

# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''
testResults = []
media = 0

testResults.append(input('Digite a nota do primeiro bimestre: '))
testResults.append(input('Digite a nota do segundo bimestre: '))
testResults.append(input('Digite a nota do terceiro bimestre: '))
testResults.append(input('Digite a nota do quarto bimestre: '))

for testResult in testResults:
    media = media + float(testResult)

media = media/len(testResults)
print(media)

'''
# 5 - Faça um Programa que converta metros para centímetros.
'''
meters = input('Digite a medida, em m, a ser convertido para cm: ')
centimeters = float(meters) * 100
print('%s m -> %f cm' % (meters, centimeters))
'''

# 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#https://wiki.python.org.br/EstruturaSequencial

# 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.