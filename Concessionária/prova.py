import funcoes
cadastro = {}
reserva = {}
verificacao = {}
cpfs = []
carros_contaodor = {'carros':20}
try:
    funcoes.txt(cadastro, 'relatorio_clientes.txt')
except FileNotFoundError:
    pass
try:
    funcoes.txt2(verificacao, 'verificar_carros.txt')
except FileNotFoundError:
    pass
try:
    funcoes.txt4(carros_contaodor, 'contador.txt')
except FileNotFoundError:
    pass
#menu
opcao = 1
print('\033[1;34m++++++++++++++++++Bem vindo a Concessionária UNIT!++++++++++++++++++')
while True:
    print('\033[1;36m Escolha uma opção do menu: ')
    print()
    print('\033[1;36m 1 - Cadastrar Cliente ')
    print('\033[1;36m 2 - Cadastro de Carros para Aluguel ')
    print('\033[1;36m 3 - Registro de Aluguel de Carro ')
    print('\033[1;36m 4 - Relatório de Clientes ')
    print('\033[1;36m 5 - Relatório de Alugueis ')
    print('\033[1;36m 0 - Sair ')
    print()
    opcao = 0
    if opcao not in ('1', '2', '3', '4', '5', '0'):
        try:
            opcao = input('Escolha sua opção: ')
        except ValueError:
            print('Digite apenas numeros!')
        if opcao == '1':
            print('Cadastrar Cliente')
            entrada = 0
            while entrada not in ('S', 'N'):  # impede de passar outras letras e numeros
                entrada = str(input('Deseja se cadastrar(S/N)?: ')).upper()
                if entrada == 'S':
                    nome = str(input('Digite seu nome: '))
                    while nome.isnumeric():
                        nome = str(input('Digite seu nome: '))
                    cpf = '0'
                    while len(cpf) != 11:
                        cpf = input('Digite seu CPF(11 digitos): ')
                        if len(cpf) == 11 and cpf not in cadastro.keys():
                            cadastro[cpf] = [nome]
                            with open('relatorio_clientes.txt', 'a') as doc:
                                doc.write(cpf)
                                doc.write(' ')
                                doc.write(f'{nome}\n')
                                print('Voce foi cadastrado!')
                        elif cpf in cadastro.keys():
                            print('Essa pessoa ja esta cadastrada!')
                        else:
                            print('CPF precisa ter 11 digitos!')
                            break
        elif opcao == '2':
            print(verificacao)
            entrada = 0
            while entrada not in ('S', 'N'):  # impede de passar outras letras e numeros
                entrada = str(input('Deseja se cadastrar(S/N)?: ')).upper()
                if entrada == 'S':
                    marca = '0'
                    while marca.isnumeric():
                        marca = str(input('Digite a marca do carro procurado: '))
                    modelo = '0'
                    while modelo.isnumeric():
                        modelo = str(input('Digite o modelo do carro procurado: '))
                    ano = '0'
                    while len(ano) != 4:
                        ano = input('Digite o ano do carro procurado: ')
                    status = 0
                    while status not in ('Disponivel', 'Indisponivel'):
                        status = str(input('Digite o status do carro (Disponivel/Indisponivel): ')).capitalize()
                    placa = input('Digite o numero a placa: ')
                    if len(placa) == 6 and placa not in verificacao.keys():
                            verificacao[placa] = [ano, modelo, marca, status]
                            with open('verificar_carros.txt', 'a') as doc:
                                doc.write(f'{str(placa)}')
                                doc.write(' ')
                                doc.write(marca)
                                doc.write(' ')
                                doc.write(modelo)
                                doc.write(' ')
                                doc.write(f'{str(ano)}')
                                doc.write(' ')
                                doc.write(f'{status}\n')
                            print('Cadastrado com sucesso!')
                    elif placa in verificacao.keys():
                        print('Esse carro ja esta cadastrado!')
                    else:
                        print('A placa tem que ter 6 digitos!')
                        break
        elif opcao == '3':
            cpf = '0'
            while len(cpf) != 11:
                cpf = input('Digite seu CPF(11 digitos): ')
                cpfs.append(cpf)
                if cpf == cpfs:
                    print('Voce so pode alugar apenas um carro.')
                    break
            placa = '0'
            while len(placa) != 6:
                placa = input('Digite o numero a placa: ')
                reserva[cpf] = [placa]
            if len(placa) == 6 and placa in verificacao.keys() and cpf in reserva.keys() \
                    and verificacao.get(placa)[3] == 'Disponivel':
                carros_contaodor['carros'] -= 1
                contador1 = list(carros_contaodor.keys())
                contador2 = list(carros_contaodor.values())
                with open('contador.txt','w') as doc:
                    for k in range(0,len(contador1)):
                        doc.write(str(contador1[k]))
                        doc.write(' ')
                        doc.write(f'{str(contador2[k])}\n')
                if carros_contaodor['carros'] <= 0:
                    print('Não ha carros disponiveis!')
                else:
                    print('Carro reservado!')
                    verificacao[placa][3] = 'Indisponivel'
                with open('reservas_carros.txt', 'a') as doc:
                    doc.write(cpf)
                    doc.write(' ')
                    doc.write(f'{str(placa)}\n')

            elif len(placa) == 6 and cpf in reserva.keys():
                print('Carro indisponivel!')

        elif opcao == '4':
            relatorio_clientes = open('relatorio_clientes.txt', 'r')
            print(relatorio_clientes.read())

        elif opcao == '5':
            relatorio_alugueis = open('reservas_carros.txt', 'r')
            print('Cpf          Placa')
            print(relatorio_alugueis.read())

        elif opcao == '0':
            print('Obrigado por estar na Concessionária UNIT!')
            break
