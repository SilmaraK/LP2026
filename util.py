def inputint(msg):
    try:
        valor = int(input(msg))
        return valor
    except ValueError:
        print ('ERRO: Valor informado não é inteiro!')
    return -1

def inputfloat(msg):
    try:
        valor = float(input(msg))
        return valor
    except ValueError:
        print ('ERRO: Valor informado não é um número real!.')
    return -1


def gerar_palavra (min: int=4,max: int=10) -> str:
    qtde_letras = random.randrange(min,max+1)
    palavra = ''
    for _ in range (qtde_letras):
        palavra += chr(random.randrange(65,91))
    return palavra

   

