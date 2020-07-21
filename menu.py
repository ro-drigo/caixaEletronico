import time


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
                    from Administração.administracao import adm
                    adm()
                elif opcao == 2:
                    from Cliente.MenuCliente import menucliente
                    menucliente()
                elif opcao == 3:
                    from Movimentação.movimento import movi
                    movi()
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