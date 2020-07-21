import os
import time
import sys


def adicionarCliente(email, nome, telefone):
    dirname = os.path.dirname(__file__)

    arquivo = open(dirname + '/db.txt', 'r')
    conteudo = arquivo.readlines()

    conteudo.append(email+','+nome+','+telefone+'\n') #insira seu conteúdo
    arquivo = open(dirname + '/db.txt', 'w') # Abre novamente o arquivo (escrita)
    arquivo.writelines(conteudo)
    arquivo.close()

    print("Usuário adicionado!")

    time.sleep(2)
    return

def alterarCliente():
    print("Em manutenção. Escolha outra opção...")
    time.sleep(2)
    return

def excluirCliente():
    print("Em manutenção. Escolha outra opção...")
    time.sleep(2)
    return

def buscarClientePeloEmail():
    print("Em manutenção. Escolha outra opção...")
    time.sleep(2)
    return

def buscarClientePeloIdentificador():
    print("Em manutenção. Escolha outra opção...")
    time.sleep(2)
    return

def listarClientes():
    print("Em manutenção. Escolha outra opção...")
    time.sleep(2)
    return

def sair():
    print("Sempre que precisar, procure-nos. Até mais!")
    time.sleep(2)
    sys.exit()


def adm():
    while True:

        print("Seja bem vindo, administrador!")
        time.sleep(2)

        print("O que deseja fazer agora?")
        time.sleep(2)

        print("=============================")

        print("1 - Adicionar Cliente")
        print("2 - Alterar Cliente")
        print("3 - Excluir Cliente")
        print("4 - Buscar Cliente Pelo E-mail")
        print("5 - Buscar Cliente Pelo Identificador")
        print("6 - Listar Todos os Clientes")
        print("7 - Sair do Sistema de Banco")

        print("=============================")

        opcaoSelecionada = int(input("Digite o opção desejada: "))

        if opcaoSelecionada == 1:

            email = input("Insira o e-mail: ")
            nome = input("Insira o nome: ")
            telefone = input("Insira o número de telefone: ")
            adicionarCliente(email, nome, telefone)

        elif opcaoSelecionada == 2:
            alterarCliente()
        elif opcaoSelecionada == 3:
            excluirCliente()
        elif opcaoSelecionada == 4:
            buscarClientePeloEmail()
        elif opcaoSelecionada == 5:
            buscarClientePeloIdentificador()
        elif opcaoSelecionada == 6:
            listarClientes()
        elif opcaoSelecionada == 7:
            sair()
        else:
            print("Opção inválida. Por favor, digite novamente...")
            time.sleep(2)
        pass
    pass

adm()