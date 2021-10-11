def txt(cadastro, documento):
    with open(f'{documento}') as dicionario:
        for line in dicionario:
            (chave, valor) = line.split()
            cadastro[chave] = valor

def txt2(cadastro, documento):
    with open(f'{documento}') as dicionario:
        for line in dicionario:
            (chave, valor, valor2, valor3, valor4) = line.split()
            cadastro[chave] = [valor, valor2, valor3, valor4]


def txt4(cadastro, documento):
    with open(f'{documento}') as dicionario:
        for line in dicionario:
            (chave, valor) = line.split()
            cadastro[chave] = int(valor)
