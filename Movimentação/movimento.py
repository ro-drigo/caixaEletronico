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
    nom = c['Nome'].split(" ")
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

c = {
    "Nconta": "",
    "Nome": "",
    "Saldo": 0.00,
    "Email": "",
    "Telefone": "",
    "Pass": ""
}

def Verifica():
    global c
    arquivo = open('../db.txt', 'r')
    for item in arquivo:
        campo = item.split(',')
        string = ""
        for i in campo[5]:
            if i != "\n":
                string += i
        campo[5] = string
        if c['Nconta'] == campo[0] and c['Pass'] == campo[5]:
            c['Nconta'] = campo[0]
            c['Nome'] = campo[1]
            sal = "%.2f" % float(campo[2])
            c['Saldo'] = float(sal)
            #Saldo = float(campo[2])
            c['Email'] = campo[3]
            c['Telefone'] = campo[4]
            c['Pass'] = campo[5]
    arquivo.close
    if c['Email'] == "":
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
    print("\t|  Nome ->", c['Nome'])
    print("\t|  Email ->", c['Email'])    
    print("\t|  Saldo -> %.2f" % c['Saldo'])
    print("\t|")
    print("\t|________________________________")

def Sacar():
    limpaTela()
    while True:
        print("\a \v")
        print("\t ____________________________________")
        print("\t|                                    |")
        print("\t|                SAQUE               |")
        print("\t|                                    |")
        print("\t|====================================|")
        print("\t|                                    |")
        print("\t|  1 - R$ 50,00    3 - R$ 100,00     |")
        print("\t|                                    |")
        print("\t|  2 - R$ 75,00    4 - Outro valor   |")
        print("\t|                                    |")
        print("\t|____________________________________|")
        print("\t|____________________________________|")
        try:
            Esc = int(input('\t| [++]>> ')) 
        except:
            print("\tErro: Número Inválido!!")
            continue
        if Esc < 1 or Esc > 4:
            print("\tErro: Número Inválido!!")
            continue
        else:
            arquivo = open('../db.txt','r')
            nsaldo = 0.0
            if Esc == 1:
                nsaldo = 50.00
            elif Esc == 2:
                nsaldo = 75.00                
            elif Esc == 3:
                nsaldo = 100.00
            else:
                while True:
                    try:
                        nsaldo = float(input("\t Digite o valor: "))
                        break
                    except:
                        print("\tErro: Número Inválido!")
                        time.sleep(2)
            global c
            for linha in arquivo:
                campo = linha.split(',')
                if campo[0] == c['Nconta']:
                    if nsaldo > c['Saldo']:
                        print("\tErro: Valor do saque maior do que o saldo!!")
                        continue
                    elif nsaldo < 25.0:
                        print("\tErro: Valor do saque inválido!!")
                        continue
                    else:
                        c['Saldo'] -= nsaldo
                        campo[2] = "%.2f" % c['Saldo']
                    arq = open("../db.txt","w")
                    arq.write('{},{},{},{},{},{}'.format(campo[0],campo[1],campo[2],campo[3],campo[4],campo[5]))
                    arq.close
                    arquivo.close
                else:
                    arq = open("../db.txt","a")
                    arq.write('{},{},{},{},{},{}'.format(campo[0],campo[1],campo[2],campo[3],campo[4],campo[5]))
                    arq.close
                    arquivo.close
                ver = Verifica()
                if ver != "":
                    print("Erro: Algo deu errado :(")
        break
        

while True:
    limpaTela()
    Login()
    c['Nconta'] = input('\t| [$número da conta$]>> ')
    c['Pass'] = input('\t| [$password$]>> ')
    ver = Verifica()
    if ver != "":
        print('\tErro: Você digitou algo errado!!')
        time.sleep(2)
        continue
    else:
        # Menu Infinito
        while True:
            limpaTela()
            Menu()
            # Verifica se é um número
            try:
                esc = int(input('\t|[++]-> '))
            except:
                print("Erro: Número Inválido!")
                time.sleep(2)
                continue
            # Verifica se o número é válido
            if esc < 1 or esc > 5:
                print("Erro: Número Inválido!")
                time.sleep(2)
                continue
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
                    Esc = input('\tTecle para continuar...')
                elif esc == 2:
                    Sacar()
                    print()
                    Esc = input('\tTecle para continuar...')
                elif esc == 3:
                    print("Depósito")
                else:
                    print("Pagamento")
                    time.sleep(2)
                    
    break
