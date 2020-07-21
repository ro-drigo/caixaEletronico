import os
import platform
import time

#Função que limpa tela
def limpaTela():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")

def Login():
    #print("\033[47m")
    #print("\033[41m")
    print("\a \v")
    print("\t __________________________________________")
    print("\t|                                          |")
    print("\t|    -----  --   __   ___ __  *            |")
    print("\t|      |   |--  | _|  |  |  | |  |\\  |     |")
    print("\t|      |    --  | \\   |  |  | |  |  \\|     |")
    print("\t|                                          |")
    print("\t|__________________________________________|")

# Função do Menu
def Menu():
    nom = Nome.split(" ")
    print("\a \v")
    print("\t __________________________________________")
    print("\t|                                          |")
    print("\t|    -----  --   __   ___ __  *            |")
    print("\t|      |   |--  | _|  |  |  | |  |\\  |     |")
    print("\t|      |    --  | \\   |  |  | |  |  \\|     |")
    print("\t|                                          |")
    print("\t|__________________________________________|")
    print("\t                                       ")
    print("\t  Seja Bem-Vindo",nom[0],"ao terminal! ")
    print("\t                                       ")
    print("\t|==========================================|")
    print("\t|                                          |")
    print("\t|   1 - Saldo       2 - Saque              |")
    print("\t|                                          |")
    print("\t|   3 - Depósito    4 - Pagamento          |")
    print("\t|                                          |")
    print("\t|   5 - Sair                               |")
    print("\t|                                          |")
    print("\t|__________________________________________|")

Nconta = 0
Nome = ""
Saldo = 0.0
Email = ""
Telefone = ""

def Verifica():        
    global Nconta
    global Nome
    global Saldo
    global Email
    global Telefone
    global Pass
    arquivo = open('../db.txt', 'r')
    for item in arquivo:
        campo = item.split(',')
        string = ""
        for i in campo[5]:
            if i != "\n":
                string += i
        campo[5] = string
        if Nconta == campo[0] and Pass == campo[5]:
            Nconta = campo[0]
            Nome = campo[1]
            sal = "%.2f" % float(campo[2])
            Saldo = float(sal)
            #Saldo = float(campo[2])
            Email = campo[3]
            Telefone = campo[4]
            Pass = campo[5]
    if Email == "":
        return "Não achamos sua conta :("
    return ""

def VerSaldo():
    limpaTela()
    print("\a \v")
    print("\t ________________________________")
    print("\t|                                |")
    print("\t|             SALDO              |")
    print("\t|                                |")
    print("\t|================================|")
    print("\t|")
    print("\t|  Nome ->", Nome)
    print("\t|  Email ->", Email)    
    print("\t|  Saldo -> %.2f" % Saldo)
    print("\t|")
    print("\t|______________________________")

while True:
    limpaTela()
    Login()
    Nconta = input('\t| [$número da conta$]>> ')
    Pass = input('\t| [$password$]>> ')
    ver = Verifica()
    if ver != "":
        print('\tErro: Você digitou algo errado!!')
        time.sleep(2)
        limpaTela()
    else:
        # Menu Infinito
        while True:
            limpaTela()
            Menu()
            # Verifica se é um número
            try:
                esc = int(input('\t|[++]-> '))
                # Verifica se o número é válido
                if esc < 1 or esc > 5:
                    print("Erro: Número Inválido!")
                    time.sleep(2)
                # Finaliza a sessão
                elif esc == 5:
                    print("Obrigado por utilizar o terminal :D")
                    print("Volte Sempre!!")
                    break
                # Chama a função escolhida
                else:
                    if esc == 1:
                        VerSaldo()
                        print()
                        esc = input('\tTecle para continuar...')
                    elif esc == 2:
                        print("Saque")
                    elif esc == 3:
                        print("Depósito")
                    else:
                        print("Pagamento")
                    time.sleep(2)
            # imprime o erro
            except:
                print("Erro: Número Inválido!")
                time.sleep(2)
        break
