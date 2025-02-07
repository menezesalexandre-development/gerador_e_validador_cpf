# PROGRAMA GERADOR DE CPF:

def gerar_cpf():
    # GERADOR DOS NOVE DÍGITOS:
    import random

    cpf_gerado = str()
    counter = 1
    while counter <= 9:
        numero_aleatorio = random.randint(0, 9)
        cpf_gerado += f'{numero_aleatorio}'
        
        counter += 1

    # VERIFICAÇÃO DO PRIMEIRO DÍGITO:
    multiplicador = 10
    multiplicados = []
    for c in range(len(cpf_gerado)): 
        if c <= 8:
            multiplicados.append(int(cpf_gerado[c]) * (multiplicador-c))
        else:
            break

    soma_mais_10 = sum(multiplicados) * 10

    resto_11 = soma_mais_10 % 11
    if resto_11 > 9:
        primeiro_digito = 0
    elif 0 <= resto_11 <= 9: 
        primeiro_digito = resto_11
    else:
        primeiro_digito = 'Não foi possível gerar o primeiro dígito do CPF'

    cpf_gerado += f'{primeiro_digito}'

    #VERIFICAÇÃO DO SEGUNDO DÍGITO:
    multiplicador = 11
    multiplicados = []
    for c in range(len(cpf_gerado)): 
        if c <= 9:
            multiplicados.append(int(cpf_gerado[c]) * (multiplicador-c))
        else:
            break

    soma_mais_10 = sum(multiplicados) * 10

    resto_11 = soma_mais_10 % 11
    if resto_11 > 9:
        segundo_digito = 0
    elif 0 <= resto_11 <= 9: 
        segundo_digito = resto_11
    else:
        segundo_digito = 'Não foi possível gerar o segundo dígito do CPF'

    cpf_gerado += f'{segundo_digito}'

    # FORMATADOR DO CPF:
    cpf_gerado = f'{cpf_gerado}'
    cpf_gerado = "{}.{}.{}-{}".format(cpf_gerado[:3], cpf_gerado[3:6], cpf_gerado[6:9], cpf_gerado[9:])

    return cpf_gerado
