'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome
def q1():
    print ('Silmara')
#q1()
    
#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q2():
    x=30
    y=27
    print (x*y)
#q2()

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q3():
    x=5                   # media = (5+8+12)/3
    y=8                   # print(f'(5+8+12)/3 = {media}')
    z=12
    print ((x+y+z)/3)
#q3()

#4. Faça um programa que leia e imprima um número inteiro.
def q4():
    numero = int(input ('Digite um número inteiro: '))
    print(f'O número é: {numero} ')
#q4()
    
#5. Faça um programa que leia dois números reais e os imprima.
def q5():
    num1 = float(input ('Digite o primeiro número real: '))
    num2 = float(input ('Digite o segundo número real: '))
    print (f'Os números são: {num1:.2f} e {num2:.2f}')
#q5()

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q6():
    num = int(input ('Digite um número inteiro: '))
    num1 = num-1
    num2 = num+1
    print(f'O número antecessor é {num1} e o sucessor é {num2}')
#q6()

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q7():
    nome = input('Digite seu nome: ')
    end = input('Digite seu endereço: ')
    tel = input('Digite seu telefone: ')
    print(f'{nome}, seu endereço é {end} e seu telefone é {tel}')
#q7()

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q8():
    num1 = int(input ('Digite o primeiro número: '))
    num2 = int(input ('Digite o segundo número: '))
    sub = num1-num2
    print(f'A diferença deles é: {sub}')
#q8()

#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q9():
    num = float(input('Digite o número real: '))
    num1 = num/4    
    print (f'1/4 do número {num} é: {num1: .2f}')
#q9()

#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    num1 = float(input('Digite o 1º número real: '))
    num2 = float(input('Digite o 2º número real: '))
    num3 = float(input('Digite o 3º número real: '))
    media = ((num1+num2+num3)/3)
    print (f'A média é: {media: .2f}')
#q10()

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    num1 = int(input('Digite o 1º número inteiro: '))
    num2 = int(input('Digite o 2º número inteiro: '))
    num3 = int(input('Digite o 3º número inteiro: '))
    num4 = int(input('Digite o 4º número inteiro: '))
    soma = num1+num2+num3+num4
    sub = num1-num2-num3-num4
    mult = num1*num2*num3*num4
    div = num1/num2/num3/num4
    print (f'O resultado da soma é: {soma}; da subtração é: {sub}; da multiplicação é: {mult} e da divisão é: {div}')
#q11()

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    num = float(input("Digite um número real: "))
    print (f'O quadrado de {num} é: {num*num: .2f}')
#q12()

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    num = float(input('Digite o saldo inicial: '))
    saldo = num * 0.02
    print (f'O saldo atualizado é de: {num + saldo: .2f}')
#q13()

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base*2 + altura*2) e a área (base * altura). 
def q14():
    base = float(input('Digite a base do retangulo: '))
    altura = float(input('Digite a altura do retangulo: '))
    print (f'O perímetro do retangulo é: {base*2 + altura*2: .2f} e da área é: {base*altura}')
#q14()

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def q15():
    valor = float(input('Digite o valor do produto: '))
    desc = float(input('Digite o % de desconto: '))
    desc1 = desc / 100
    desc2 = valor*desc1
    print(f'O valor final é {valor-desc2: .2f}')
#q15()

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
def q16():
    sal= float(input('Digite o valor do salário: '))
    reaj = float(input('Digite o % de reajuste: '))
    reaj1 = reaj / 100
    reaj2 = sal*reaj1
    print(f'O valor final de salário é {sal+reaj2: .2f}')
#q16()

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5
def q17():
    c = float(input('Digite a temperatura atual em Celsius: '))
    f = (9*c+160)/5
    print (f'A temperatura em Fahrenheit é: {f: .1f}')
#q17()

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
def q18(): 
    tempo = float(input('Digite o tempo gasto em horas: '))
    vel = int(input('Digite a velocidade média: '))
    d = tempo*vel
    l = d/12
    print(f'A distância percorrida foi {d: .1f}km e consumiu {l: .1f} litros')
#q18()
   
#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
def q19():
    prest = float(input('Digite o valor da prestação: '))
    dias = int(input('Digite os dias em atraso: '))
    juros = float(input('Digite o % de juros: '))
    jur1 = juros / 100
    jur2 = prest*jur1
    dias1 = jur2*dias
    print(f'O valor final da prestação é {prest+dias1: .2f}')
#q19()

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar
def q20():
    real = float(input('Digite o valor em real R$: '))
    dolar = float(input('Digite o valor da cotação em dólar U$: '))
    real1 = real/dolar
    print(f'O valor em dólar é R$:{real1: .2f}')

#q20()