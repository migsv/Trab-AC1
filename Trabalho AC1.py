#Elabore uma eq do 2°, ''ax² + bx + c = 0''

print('Olá, sou a calculadora de equações do 2°!')
print('Digite os valores de a, b e c: ')
a = int(input('Digite aqui o valor de a: '))
b = int(input('Digite aqui o valor de b: '))
c = int(input('Digite aqui o valor de c: '))
delta = b**2 - 4 * a * c
bhask = (-1*b + delta ** 0.5) / (2*a)
bhask2 = (-1*b - delta ** 0.5) / (2*a)
print(delta, bhask, bhask2)

'''
Elabore um programa que leia uma variável inteira ano.
Em seguida, exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto. 
Um ano é bissexto se ele é múltiplo de quatro. No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. 
Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.
'''
print('Olá! Vou te dizer se um ano é bissexto ou não!')
ano = int(input('Digite o valor de um ano: '))
bis = (ano % 4 == 0) and ano % 100 != 0 or ano % 400 == 0
print('Caso de True é um ano bissexto, caso de False, não é.')
print(bis)
