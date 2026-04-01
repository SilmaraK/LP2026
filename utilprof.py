def inputint(msg="Digite um valor inteiro: ",min=None,max=None):
    erro = True
    while erro == True:
        try:
            valor = int(input(msg))
            if min!=None and type(min)!=int:
                raise Exception(f'ERRO: O valor mínimo deve ser inteiro e não {min}')
            if max!=None and type(max)!=int:
                raise Exception(f'ERRO: O valor máximo deve ser inteiro e não {max}')
            if min!=None and valor < min:
                raise Exception(f'ERRO: valor é menor do que o mínimo permitido de {min}')
            if max!=None and valor > max:
                raise Exception(f'ERRO: valor é maior do que o máximo permitido de {max}')
            erro = False
            return valor
        except ValueError:
            print ('ERRO: Valor informado não é inteiro!')
        except Exception as e:
            print(e)

def inputfloat(msg="Digite um número real: ",min=None,max=None):
    try:
        valor = float(input(msg))
        if min!=None and valor < min:
            raise Exception(f'ERRO: valor é menor do que o mínimo permitido de {min}')
        if max!=None and valor > max:
            raise Exception(f'ERRO: valor é maior do que o máximo permitido de {max}')
        return valor
    except ValueError:
        print ('ERRO: Valor informado não é um número real!')
    except Exception as e:
        print(e)
    return -1

def gerar_palavra(min: int=4,max: int=10) -> str:
    qtde_letras = random.randrange(min,max+1)
    palavra=''
    for _ in range(qtde_letras):
        palavra += chr(random.randrange(65,91))
    return palavra