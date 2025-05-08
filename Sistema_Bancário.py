menu = """

Menu Principal
Selecione a operação desejada:

[1] Depositar
[2] Sacar   
[3] Extrato
[0] Sair

 """

saldo = 0
limite = 500
real_saldo = saldo + limite
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0
valor = 0
excedeu_saques = 0

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Quanto deseja depositar? R$ "))
    
        if valor > 0:
            saldo += valor  
            extrato += f"Deposito de R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2": 
        print("====== Saques ======")
        valor = float(input("Quanto deseja sacar? R$ "))

        excedeu_saques = numero_saques >= LIMITE_SAQUES 
        
        if valor > real_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_saques:
            print("Operação falhou! Você já atingiu o limite de saques diários.")
        
        elif valor <= real_saldo:
            extrato += f"Saque de R$ {valor:.2f}\n"
            print(f"saque de R$ {valor:.2f} realizada com sucesso!")
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("====== Extrato ======")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)   
    
    elif opcao == "0":
       print("Obrigado por utilizar nosso sistema!")
       print("Volte sempre!")
       break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")