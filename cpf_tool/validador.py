
# PROGRAMA VALIDADOR DE CPF

def validar_cpf(cpfDigitado):
    # INSERÇÃO DO CPF
    cpf = str(cpfDigitado)
    cpf = str(cpf.replace(".","").replace("-",""))

    # VERIFICAÇÃO DO PRIMEIRO DÍGITO:
    multiplicador = 10
    multiplicados = []
    for c in range(len(cpf)): 
        if c <= 8:
            multiplicados.append(int(cpf[c]) * (multiplicador-c))
        else:
            break

    soma_mais_10 = sum(multiplicados) * 10

    resto_11 = soma_mais_10 % 11
    if resto_11 > 9:
        primeiro_digito = 0
    elif 0 < resto_11 < 9: 
        primeiro_digito = resto_11
    else:
        primeiro_digito = 'Não foi possível gerar o primeiro dígito do CPF'

    #VERIFICAÇÃO DO SEGUNDO DÍGITO: 
    multiplicador = 11
    multiplicados = []
    for c in range(len(cpf)): 
        if c <= 9:
            multiplicados.append(int(cpf[c]) * (multiplicador-c))
        else:
            break

    soma_mais_10 = sum(multiplicados) * 10

    resto_11 = soma_mais_10 % 11
    if resto_11 > 9:
        segundo_digito = 0
    elif 0 < resto_11 < 9: 
        segundo_digito = resto_11
    else:
        segundo_digito = 'Não foi possível gerar o primeiro dígito do CPF'

    # VALIDAÇÃO DO CPF:
    cpf_calculado = f'{cpf[:9]}{primeiro_digito}{segundo_digito}'

    if (cpf_calculado == cpf) and (primeiro_digito == int(cpf[9]) and segundo_digito == int(cpf[10])):
        situacao = 'válido'
    else:
        situacao = 'inválido'

    return (f'O CPF "{cpfDigitado}" é {situacao}')
