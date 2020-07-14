import os
import time

def carregar_cliente():
    lista = []

    try:
        arquivo = open("clientes.txt", "r")

        for linha in arquivo.readlines(): #armazena em linha a o valor da linha
            coluna = linha.strip().split("#") #coluna recebe agora um vetor
            cliente = {
                "email": coluna[1],
                "nome": coluna[0],
                "tel": coluna[2]
            }
            lista.append(cliente)

        arquivo.close()
    except FileNotFoundError:
        print("Arquivo não existe - Criar....")
        pass

    return lista

def salvar_cliente(lista):

    arquivo = open("clientes.txt", "w")#se não existir arquivo cria um novo

    for cliente in lista:
        arquivo.write('{}#{}#{}\n'.format(cliente['nome'], cliente['cnpj'], cliente['email']))

    arquivo.close()

def existe_cliente(lista, cnpj):
    if len(lista) > 0:
        for cliente in lista:
            if cliente['cnpj'] == cnpj:
                 return True
    return False

def adicionar(lista):
    while True:
        cnpj = input("Digite o CNPJ do Banco/Fintech: ")

        if not existe_cliente(lista, cnpj):
            break
        else:
            print("Esse CNPJ já foi utilizado.")
            time.sleep(2)

    cliente = {
        "cnpj": cnpj,
        "nome": input("Digite o nome do Banco/Fintech: "),
        "email": input("Digite o email de contato: ")
    }

    lista.append(cliente) #adiciona no final da lista

    print("{} foi cadastrado com sucesso!\n".format(cliente['nome']))
    time.sleep(2)
    os.system("cls")

def listar(lista):
    print("==Lista de Clientes==")
    if len(lista) > 0:
        for i, cliente in enumerate(lista):
            print("Cliente {}".format(i+1))
            print("\tNome: {}".format(cliente['nome']))
            print("\tCNPJ: {}".format(cliente['cnpj']))
            print("\tEmail de contato: {}".format(cliente['email']))
            print("===============================================")
        print("Quantidade de Clientes: {}\n".format(len(lista)))
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def menucliente():
    lista = carregar_cliente()
    while True:
        time.sleep(2)
        os.system("cls")
        print("======== MENU CLIENTE =======")
        print("1 - Cadastrar Banco ou Fintech")
        print("2 - Alterar Banco ou Fintech")
        print("3 - Listar Bancos e Fintechs")
        print("4 - Excluir Banco ou Fintech")
        print("5 - Sair do Sistema de Cliente")
        print("==============================")
        try:
            opcao = int(input("Digite o opção desejada: "))
            if 1 <= opcao <= 5:
                if opcao == 1:
                    adicionar(lista)
                    salvar_cliente(lista)
                elif opcao == 2:
                    print("Não programado ainda.")
                elif opcao == 3:
                    listar(lista)
                elif opcao == 4:
                    print("Não programado ainda.")
                else:
                    print("Saindo do Menu Cliente...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("Êxito em sair do Sistema Cliente.")
                    break
            else:
                print("A entrada não pertence a uma das opções.")
        except:
            print("A entrada não é válida.")

def menup():
    while True:
        print("======== MENU =======")
        print("1 - Administrativo")
        print("2 - Cliente")
        print("3 - Movimentação")
        print("4 - Sair do Menu")
        print("=====================")

        try:
            opcao = int(input("Digite o opção desejada: "))
            if 1 <= opcao <= 4:
                if opcao == 1:
                    print("=D")
                elif opcao == 2:
                    menucliente()
                elif opcao == 3:
                    print("=D")
                else:
                    print("Saindo do Menu...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("Êxito em sair do Menu.")
                    break
            else:
                print("A entrada não pertence a uma das opções.")
        except:
            print("A entrada não é válida.")

menup()