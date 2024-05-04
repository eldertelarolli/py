menu =  """ 

[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair


=> """


saldo = 0
limite = 500
extrato =  ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito"))

        if valor > 0 :
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
        else:
            print("Operação falhou! o valor informado é invalido.")
    elif opcao == "s":
        valor=float(input("Informe o valor de saque: "))

        execedeu_saldo = valor > saldo
        execedeu_limite = valor > limite
        execedeu_saques = numero_saques >= LIMITE_SAQUES

        if execedeu_saldo :
            print("Operação falhou! Voce nao tem saldo suficiente")
        
        elif execedeu_limite:
            print("Operação falou ! voce nao possui limite ")

        elif valor > 0 :
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques +=1
        else:           
            print("Operacao falhou! o valor informado é invalido.")
    
    elif opcao == "e":
        print("\n==================Extrato==================")
        print("Não foram realizadas movimentações. " if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================") 
    elif opcao == "q":
        break            

    else:
        print("Operacao invalida , por favor selecione novamente a operacao desejada .")    