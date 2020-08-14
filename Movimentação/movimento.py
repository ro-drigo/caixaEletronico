import os
import platform
import time
from datetime import datetime

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
    print("\t|   5 - Ver Pagamentos     0 - Sair        |")
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
l = {
    "Nconta": "",
    "Nome" : "",
    "Preco": 0.0,
    "Data": ""
}


def Verifica():
    global c
    arquivo = open('db.txt', 'r')
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
        return "\tNão achamos sua conta :("
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
        print("\t|      Tecle 0 para retornar...      |")
        print("\t|____________________________________|")
        print("\t|____________________________________|")
        try:
            Esc = int(input('\t| [++]>> ')) 
        except:
            print("\tErro: Número Inválido!!")
            continue
        if Esc == 0:
            print("Returning...")
            time.sleep(2)
            break
        if Esc < 0 or Esc > 4:
            print("\tErro: Número Inválido!!")
            continue
        else:
            arquivo = open('db.txt','r')
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
                        if nsaldo < 5:
                            print("\tErro: Número Inválido!")
                            time.sleep(2)
                            continue
                        break
                    except:
                        print("\tErro: Número Inválido!")
                        time.sleep(2)
                        continue
            global c
            for linha in arquivo:
                campo = linha.split(',')
                if campo[0] == c['Nconta']:
                    if nsaldo > c['Saldo']:
                        print("\tErro: Valor do saque maior do que o saldo!!")
                        continue
                    elif nsaldo < 5.0:
                        print("\tErro: Valor do saque inválido!!")
                        continue
                    else:
                        c['Saldo'] -= nsaldo
                        campo[2] = "%.2f" % c['Saldo']
                    arq = open("db.txt","w")
                    arq.write('{},{},{},{},{},{}'.format(campo[0],campo[1],campo[2],campo[3],campo[4],campo[5]))
                    arq.close
                    arquivo.close
                    print("\tSaque realizado com sucesso!!")
                    print("\tSaldo -> R$ ",c['Saldo'])
                else:
                    arq = open("db.txt","a")
                    arq.write('{},{},{},{},{},{}'.format(campo[0],campo[1],campo[2],campo[3],campo[4],campo[5]))
                    arq.close
                    arquivo.close
                ver = Verifica()
                if ver != "":
                    print("\tErro: Algo deu errado :(")
        break

def Deposito():
    limpaTela()
    while True:
        print("\a \v")
        print("\t ____________________________________")
        print("\t|                                    |")
        print("\t|             DEPOSITO               |")
        print("\t|                                    |")
        print("\t|====================================|")
        print("\t|                                    |")
        print("\t|  1 - R$ 50,00    3 - R$ 100,00     |")
        print("\t|                                    |")
        print("\t|  2 - R$ 75,00    4 - Outro valor   |")
        print("\t|                                    |")
        print("\t|      Tecle 0 para retornar...      |")
        print("\t|____________________________________|")
        print("\t|____________________________________|")
        try:
            Esc = int(input('\t| [++]>> ')) 
        except:
            print("\tErro: Número Inválido!!")
            time.sleep(2)
            continue
        if Esc == 0:
            print("Returning...")
            time.sleep(2)
            break
        if Esc < 0 or Esc > 4:
            print("\tErro: Número Inválido!!")
            time.sleep(2)
            continue
        else:
            arquivo = open('db.txt','r')
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
                        if nsaldo < 5:
                            continue
                        break
                    except:
                        print("\tErro: Número Inválido!")
                        time.sleep(2)
            global c
            for linha in arquivo:
                campo = linha.split(',')
                if campo[0] == c['Nconta']:
                    if nsaldo < 5.0:
                        print("\tErro: Valor do saque inválido!!")
                        continue
                    else:
                        c['Saldo'] += nsaldo
                        campo[2] = "%.2f" % c['Saldo']
                    arq = open("db.txt","w")
                    arq.write('{},{},{},{},{},{}'.format(campo[0],campo[1],campo[2],campo[3],campo[4],campo[5]))
                    arq.close
                    arquivo.close
                    print("\tDepósito realizado com sucesso!!")
                    print("\tSaldo -> R$ ",c['Saldo'])
                else:
                    arq = open("db.txt","a")
                    arq.write('{},{},{},{},{},{}'.format(campo[0],campo[1],campo[2],campo[3],campo[4],campo[5]))
                    arq.close
                    arquivo.close
                ver = Verifica()
                if ver != "":
                    print("\tErro: Algo deu errado :(")
        break

def Pagamento():
    while True:
        limpaTela()
        print("\a \v")
        print("\t ____________________________________")
        print("\t|                                    |")
        print("\t|             PAGAMENTO              |")
        print("\t|                                    |")
        print("\t|====================================|")
        print("\t|      Tecle 0 para retornar...      |")
        print("\t|____________________________________|")
        global l
        global c
        print()
        l["Nome"] = input('\tDigite o nome da conta: ') 
        if len(l["Nome"]) < 3 and l["Nome"] != "0":
            print("\tErro: Número Inválido!!")
            time.sleep(2)
            continue
        elif l["Nome"] == "0":
            print("Returning...")
            time.sleep(2)
            break
        else:
            arquivo = open('db.txt','r')
            try:
                l["Preco"] = float(input("\tDigite o valor a ser pago: R$ "))
            except:
                print("\tErro: Número Inválido!!")
                time.sleep(2)
                continue
            now = datetime.now()
            format = "%d/%m/%Y %H:%M:%S"
            l["Data"] = now.strftime(format)
            for linha in arquivo:
                campo = linha.split(',')
                if campo[0] == c['Nconta']:
                    c['Saldo'] -= l["Preco"]
                    campo[2] = "%.2f" % c['Saldo']
                    arq = open("db.txt","w")
                    arq.write('{},{},{},{},{},{}'.format(campo[0],campo[1],campo[2],campo[3],campo[4],campo[5]))
                    arq.close
                    arquivo.close
                    print("okay")
                else:
                    arq = open("db.txt","a")
                    arq.write('{},{},{},{},{},{}'.format(campo[0],campo[1],campo[2],campo[3],campo[4],campo[5]))
                    arq.close
                    arquivo.close
            print("\tDepósito realizado com sucesso!!")
            print("\tSaldo -> R$ ",c['Saldo'])
                            
            formpreco = "%.2f" % l['Preco']
            arq = open("log.txt","a")
            arq.write('{},{},{},{}\n'.format(l["Nconta"],l["Nome"],formpreco,l["Data"]))
            arq.close
            arquivo.close
            print("\tPagamento realizado com sucesso!!")
            print("\tSaldo -> R$ ",c['Saldo'])
            
            ver = Verifica()
            if ver != "":
                print("\tErro: Algo deu errado :(")

        break

def VerLogs():
    global l
    print("\a \v")
    print("\t ________________________________")
    print("\t|                                |")
    print("\t|         VER PAGAMENTO          |")
    print("\t|                                |")
    print("\t|================================|")
    arquivo = open("log.txt",'r')
    for line in arquivo:
        campo = line.split(",")
        if campo[0] == l["Nconta"]:
            print("\t| \a")
            print("\t|  Nome ->", campo[1])
            print("\t|  Valor -> R$", campo[2])
            print("\t|  Data ->", campo[3])
            print("\t| \a")
    print("\t|________________________________")

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
        l["Nconta"] = c["Nconta"]  
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
            if esc < 0 or esc > 5:
                print("Erro: Número Inválido!")
                time.sleep(2)
                continue
            # Finaliza a sessão
            elif esc == 0:
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
                    Deposito()
                    print()
                    Esc = input('\tTecle para continuar...')
                elif esc == 4:
                    Pagamento()
                    print()
                    Esc = input('\tTecle para continuar...')
                else:
                    VerLogs()
                    print()
                    Esc = input('\tTecle para continuar...')
    break
