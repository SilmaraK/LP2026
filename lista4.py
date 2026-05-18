
import random
from utilprof import inputint, inputfloat, gerar_palavra
from typing import Final
import math

'''
Lista de Exercícios referentes a coleções e arquivos em python
'''

#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
def q1() -> None:
    numeros: list = [random.randrange(200) for _ in range(15)]
    print(numeros)
    numero: int = inputint ('Digite o número a ser localizado na lista: ')
    try:
         posicao: int = numeros.index(numero)
    except ValueError:
        print('Número não encontrado!')
    else: 
        print(f'Número localizado na posição: {posicao}')
            

#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada. (ASCII 65-90)
def q2() -> None:
    letras: list = [chr(random.randrange(65,91)) for _ in range (10)]
    for posicao,letra in enumerate(letras):
        print(f'[{posicao}]: {letra}')

#2.1 Faça um programa que peça ao usuário para informar a qtde de caracteres
# para a geração de uma senha aleatória. Ao final o programa deve exibir a
# senha sugerida. (ASCII 40-126)
def q21() -> None:
    tamanho_senha: int = inputint('Informe a qtde de caracteres para a senha (4-32): ', min=4, max=32)
    senha = [chr(random.randrange(40,127)) for _ in range (tamanho_senha)]
    print(f'Senha: {"".join(senha)}')
    

#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
def q3() -> None:
    numeros: list = [random.randrange(200) for _ in range(15)]
    for posicao, numero in enumerate(numeros):
        print(f'[{str(posicao):<2}]: {str(numero):>3} ({"PAR" if numero%2==0 else "IMPAR"})')


#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.
def q4() -> None:
    numeros: list[int] = [random.randrange(100) for _ in range(8)]
    print(numeros)
    for n in numeros:
        if n % 6 == 0:
            total_multiplos = total_multiplos + 1
    print(f'Total de múltiplos de seis: {total_multiplos}')

    

#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
def q5():
    alunos: list[dict] = []
    # alimenta uma lista com 15 alunos
    for c in range(1,16):
        aluno: dict = dict()
        aluno["matricula"]:int = c
        aluno["nome"]:str = gerar_palavra(max=5)
        aluno["nota1"]: float = round(random.random()*10,1)
        aluno["nota2"]:float = round(random.random()*10,1)
        aluno["media"]:float = round((aluno["nota1"] + aluno["nota2"])/2,1)
        aluno["situacao"]:str = "Aprovado" if aluno["media"] >= 6 else "Reprovado"
        alunos.append(aluno)
    # Percorrer a lista de alunos para imprimir o diário
    print("MAT\tNOME\tN1\tN2\tMD\tST")
    for aluno in alunos:
        print(f'{aluno["matricula"]}\t{aluno["nome"]}\t{aluno["nota1"]}\t{aluno["nota2"]}\t{aluno["media"]}\t{aluno["situacao"]}')

     


#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.
def q6() -> None:
    funcionarios: list [dict] = []
    for c in range(1,21):
        funcionario: dict = {}
        funcionario ["matricula"]: int = c
        funcionario["nome"]: str = gerar_palavra(max=5)
        funcionario ["salario"]: float = round(random.random()*1000,2)
        funcionario["reajuste"]: float = round((funcionario["salario"])*1.08,2)
        funcionarios.append(funcionario)
    print("MAT\tNOME\tSAL\tREAJ")
    for funcionario in funcionarios:
        print(f'{funcionario["matricula"]}\t{funcionario["nome"]}\t{funcionario['salario']}\t{funcionario['reajuste']}')




#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%
def q7() -> None:
    produtos: list[dict] = []
    for c in range(1,101):
        produto: dict = {}
        produto ["relacao"]: int = c
        compra: float = round(random.uniform(10,100),2) 
        valor_venda = 0
        while valor_venda <= compra[c]:                                                    #incluir laço de repetição (while) para usar apenas os valores que forem  
            valor_venda = round(compra * random.uniform(1.05, 1.40), 2)                        # superiores ao valor de compra
            print(f"Produto {c}: Compra {compra} | Venda {venda}")
        produto ["compra"] = compra
        produto ["venda"] = venda
        produtos.append(produto)
    lucro_menor:float = 0
    lucro_medio:float = 0
    lucro_maior:float = 0
    for p in produtos:
        lucro_valor = p["venda"]-p["compra"]
        percentual_lucros: float = ((lucro_valor / p["compra"])*100)
        if percentual_lucros < 10:
            lucro_menor += 1
        elif percentual_lucros <= 20:
            lucro_medio += 1
        else:
            lucro_maior += 1
    print(f'RELATÓRIO DE LUCRO')
    print(f'Lucro menor que 10%: {lucro_menor} produtos')
    print(f'Lucro médio entre 10 a 20%: {lucro_medio} produtos')
    print(f'Lucro maior acima de 20%: {lucro_maior} produtos')
    
    
 


#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.
def q8() -> None:
    qtde_produtos: int = 5
    produtos: list[dict] = []
    #xqtde = []
    #yvalor_compra = []
    #xqtde = []
    #yvalor_venda = []
    with open('resultado_q8.txt','a') as arquivo: 
        arquivo.write('========================\n')
        print('COD\tQTDE\tV_COMPRA\tV_VENDA\t')
        arquivo.write('COD\tQTDE\tV_COMPRA\tV_VENDA\t\n')
        for c in range (qtde_produtos):
            produto:dict = dict()
            produto["codigo"] = c
            produto["qtde"] = (random.randint(1,51))
            produto["valor_compra"]: list[float] = round(random.random()*5000,2) #for _ in range(qtde_produtos)]
            produto["valor_venda"] : list[float] = round(random.random()*10000,2)
            print(f'{produto["codigo"]}\t{produto["qtde"]}\t{produto["valor_compra"]:>8}\t{produto["valor_venda"]:<1}\t')
            arquivo.write(f'{produto["codigo"]}\t{produto["qtde"]}\t{produto["valor_compra"]:>8}\t{produto["valor_venda"]:<1}\t\n')
    #for produto in produtos:
        #print(f'{produto["codigo"]}\t{produto["qtde"]}\t{produto["valor_compra"]}\t{produto["valor_venda"]}\t')    
    
        #for posicao, numero in enumerate(produtos):      
        #    print(f'[{str(posicao):<2}]: {str(produto):>3} 
        #    arquivo.write(f'[{str(posicao):<2}]: {str(produto):>3} 



#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.
def q9() -> None:
    listaA = []
    listaB = []
    comuns = []
    for i in range(10):
        listaA.append(random.randint(1,30))
        listaB.append(random.randint(1,30))
    print(f'Lista A: {listaA} ')
    print(f'Lista B: {listaB}')

    for elemento in listaA:
        if elemento in listaB:
            if elemento not in comuns:
                comuns.append(elemento)
    #print(f'Elementos comuns: {comuns}')  - se ficar aqui em cima não grava no arquivo
    with open('resultado_q9.txt','a') as arquivo: 
        arquivo.write('========================\n')
        print(f'Elementos comuns: {comuns}')
        arquivo.write(f'Elementos comuns: {comuns}\t\n')


#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.
def q10():
    lista_original: int = []
    for i in range (10):
        lista_original.append(random.randint(1,30))
    print(f'Lista Original (aleatória): {lista_original}')
    fatorial = [math.factorial(i) for i in lista_original]
    print(f'Lista Fatorial: {fatorial}')
    maior = max(fatorial)
    menor = min(fatorial)
    media = sum(fatorial)/len(fatorial)
    print(f'Maior: {maior}    Menor: {menor}    Media: {media}\n')
    cont_pares = sum(1 for f in fatorial if f % 2 == 0)
    percentual_pares = (cont_pares / len(fatorial)) * 100
    print(f'Percentual de Pares: {percentual_pares:.1f}%')



#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.
def q11() -> None:
    lista_original: int = []
    for i in range (10):
        lista_original.append(random.randint(1,30))
    print(f'Lista Original (aleatória): {lista_original}')
    maior = lista_original[0]
    menor = lista_original[0]
    soma = 0
    contarPares = 0
    totalElementos = len(lista_original)
    for num in lista_original:
        if num > maior: 
            maior = num
        if num < menor:
            menor = num
        soma += num
        if num % 2 == 0:
            contarPares += 1
    media = soma / totalElementos
    percentualPares = (contarPares/totalElementos) *100
    with open('resultado_q11.txt','a') as arquivo: 
        arquivo.write('========================\n')
        arquivo.write (f'Maior número: {maior}\t\n')
        arquivo.write (f'Maior número: {maior}\t\n')
        arquivo.write (f'Menor número: {menor}\t\n')
        arquivo.write (f'Média dos elementos: {media}\t\n')
        arquivo.write (f'Percentual de números pares: {percentualPares:.2f}\t\n')
    
    print(f'Maior número: {maior}\t')
    print(f'Menor número: {menor}\t')
    print(f'Média dos elementos: {media}\t')
    print(f'Percentual de números pares: {percentualPares:.2f}\t')



#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.





#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.






#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.
def q14() -> None:
    lista_original: int = []
    for i in range (10):
        lista_original.append(random.randint(1,30))
    print(f'Lista Original (aleatória): {lista_original}')
    lista_quadrados: list[int] = []
    for num in lista_original:
        quadrado = num*2
        lista_quadrados.append(quadrado)
    print(f'Lista dos Quadrados: {lista_quadrados}')







#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.



#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média
def q16() ->None:
    lista_reais: list[float] = []
    soma_total = 0.0
    for i in range (10):
        num = random.uniform(10.0,50.0)
        num = round(num,1)
        lista_reais.append(num)
        soma_total += num
    media = soma_total/10
    print(f'Lista Original:  {lista_reais[:10]}')
    print(f'Média: {media:.2f}\n')
#terminar, ainda inacabado


#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#uma lista e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.

questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')