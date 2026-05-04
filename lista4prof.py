import random
from utilprof import inputint, inputfloat, gerar_palavra
from typing import Final

'''
Lista de Exercícios referentes a coleções e arquivos em python
'''

#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
     alunos: list[dict] = []
    # alimenta uma lista com 15 alunos
    for c in range(1,16):
        aluno: dict = dict()
        aluno["matricula"] = c
        aluno["nome"] = gerar_palavra(max=5)
        aluno["nota1"] = round(random.random()*10,1)
        aluno["nota2"] = round(random.random()*10,1)
        aluno["media"] = round((aluno["nota1"] + aluno["nota2"])/2,1)
        aluno["situacao"] = "Aprovado" if aluno["media"] >= 6 else "Reprovado"
        alunos.append(aluno)
    # Percorrer a lista de alunos para imprimir o diário
    print("MAT\tNOME\tN1\tN2\tMD\tST")
    for aluno in alunos:
        print(f'{aluno["matricula"]}\t{aluno["nome"]}\t{aluno["nota1"]}\t{aluno["nota2"]}\t{aluno["media"]}\t{aluno["situacao"]}')
