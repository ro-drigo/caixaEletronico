import os

import time

print("Bem-vindo!")

#@@ -31,9 +31,34 @@ def init(req):
def init(req):
  pass

def saqueCliente(req):
    dinheiro = {
      input("Informe o quanto gostaria de sacar: ")
    }
    dirname = os.path.dirname(_file_)
    filename = os.path.join(dirname, 'dinheiroNaMaquina.txt')


    arquivo = open(filename, 'r')
    quantidadeNoCaixa = arquivo.read()
    print("Quantidade disponível no caixa: "+quantidadeNoCaixa)
    arquivo.close()

    int(float(quantidadeNoCaixa))

    dinheiro = int(input("Informe o quanto gostaria de sacar: "))

    if dinheiro<=int(float(quantidadeNoCaixa)):
      arquivoEscrita = open(filename, 'w')
      #arquivoEscrita.seek(0)
      quantidade = int(float(quantidadeNoCaixa))-dinheiro
      arquivoEscrita.write(str(quantidade))
      #arquivoEscrita.truncate()
      arquivoEscrita.close()
      print("Operação concluida com sucesso. Você sacou: "+"R$"+str(dinheiro))
    else:
      print("Quantidade não disponível. Por favor, insira manualmente mais dinheiro, ou tente novamente mais tarde")




    time.sleep(2)
    pass

def depositoCliente(req):
    quantidade = {
      input("Informe o quanto gostaria de depositar: "),
      input("Informe a conta para onde o depóstio irá: "),
    }
    pass

def pagamentoCliente(req):
    pag = {
      input("Informe o quanto será pago: "),
      input("Informe a conta para onde o pagamento irá: "),
    }
    pass

print('Bem-vindo, obrigado por se juntar a nós!')
print ('1- 1.030 \n2- 2.060 \n3- 3.090 \n4- 4.120')
sala = int(input('Aproximadamente quantos salários mínimos você ganha? '))

if sala == 1:
    salmin = 1031
if sala == 2:
    salmin = 2060
if sala == 3:
    salmin = 3090
if sala == 4:
    salmin = 4120
    
print('1- Saque \n2- Depósito \n3- Pagamento \n4- sair')
proc = int(input('Digite o procedimento a ser realizado: '))


if proc == 1: 
    cont = int(input('Digite o valor do saque: '))
    if cont > salmin: 
        print('Saldo insuficiente :(')
        print('Fim')
    elif cont <= salmin:
        print('Saque realizado com sucesso :)')
        print('Fim')
if proc == 2:
    ncont = str(input('Digite o número da conta: '))
    cont = float(input('Digite o valor a ser depositado: '))
    print('Valor depositado com sucesso:')
    print('Fim')
if proc == 3:
    ncont = str(input('Digite o nome da conta a ser paga: '))
    cont = float(input('Digite o valor da conta: '))
    if cont > salmin:
        print('Saldo insuficiente :(')
        print('Fim')
    else:
        print('Conta paga com sucesso!')
        print('Fim')
