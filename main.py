from cpf_tool import gerar_cpf, validar_cpf

cpf_gerado = gerar_cpf()
verif_cpf = validar_cpf(cpf_gerado)

print(f'CPF Gerado: {cpf_gerado}')
print(verif_cpf)