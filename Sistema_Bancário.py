menu = """

Menu Principal
Selecione a operação desejada:

[1] Depositar
[2] Sacar   
[3] Extrato
[0] Sair

 """
# Sistema Bancário Simples
# O sistema permite que o usuário faça depósitos, saques e consulte o extrato de sua conta.
saldo = 0
# Definido vareável saldo 
# O saldo pode ser alterado com depósitos e saques.
limite = 500
# Definido limite de saque como 500,00
real_saldo = saldo + limite
# O saldo real é a soma do saldo e do limite de saque.
# O saldo real é utilizado para verificar se o usuário tem saldo suficiente para realizar um saque.
extrato = ""
# O extrato é uma string que armazena todas as movimentações realizadas pelo usuário.
# O extrato é atualizado a cada depósito e saque realizado.
numero_saques = 0
# O número de saques realizados pelo usuário é inicializado como 0.
# O número de saques é utilizado para verificar se o usuário atingiu o limite de saques diários.
LIMITE_SAQUES = 3
# O limite de saques diários é definido como 3.
deposito = 0
# Definido vareável saldo 
valor = 0
# Definido vareável valor
# O valor é utilizado para armazenar o valor do depósito ou saque realizado pelo usuário.
excedeu_saques = 0
# O excedeu saques é utilizado para verificar se o usuário atingiu o limite de saques diários.
# Definido vareável excedeu_saques

while True:
    opcao = input(menu)
    # O menu é exibido para o usuário e a opção escolhida é armazenada na variável opcao.
    # O menu é exibido em um loop infinito, permitindo que o usuário realize várias operações até escolher sair.
    
    if opcao == "1":
        valor = float(input("Quanto deseja depositar? R$ "))
    
        if valor > 0:
            saldo += valor  
            extrato += f"Deposito de R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    
        else:
            print("Operação falhou! O valor informado é inválido.")

# Se o usário escolher a opção 1, o sistema solicitará o valor do depósito.
# Se o valor for maior que 0, o depósito será realizado e o extrato será atualizado.
# Se o valor for menor ou igual a 0, o sistema exibirá uma mensagem de erro.
# Se o usário digitar um valor inválido, o sistema exibirá uma mensagem de erro.

    elif opcao == "2": 
        print("====== Saques ======")
        valor = float(input("Quanto deseja sacar? R$ "))

        excedeu_saques = numero_saques >= LIMITE_SAQUES 
        
        if valor > real_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_saques:
            print("Operação falhou! Você já atingiu o limite de saques diários.")
        
        elif valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        
        elif valor <= real_saldo:
            extrato += f"Saque de R$ {valor:.2f}\n"
            print(f"saque de R$ {valor:.2f} realizada com sucesso!")
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

# Se o usário escolher a opção 2, o sistema solicitará o valor do saque.
# Se o valor for maior que o saldo real, o sistema exibirá uma mensagem de erro.
# Se o número de saques realizados for maior ou igual ao limite de saques diários, o sistema exibirá uma mensagem de erro.
# Se o valor for menor ou igual ao saldo real, o saque será realizado e o extrato será atualizado.
# Se o valor for menor ou igual a 0, o sistema exibirá uma mensagem de erro.

    elif opcao == "3":
        print("====== Extrato ======")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)   
    
    # Se o usário escolher a opção 3, o sistema exibirá o extrato.
    # Se o extrato estiver vazio, o sistema exibirá uma mensagem informando que não foram realizadas movimentações.
    # Se o extrato não estiver vazio, o sistema exibirá o extrato.
    # O extrato é atualizado a cada depósito e saque realizado.

    elif opcao == "0":
       print("Obrigado por utilizar nosso sistema!")
       print("Volte sempre!")
       break

    # Se o usário escolher a opção 0, o sistema exibirá uma mensagem de agradecimento e encerrará o loop.
    # O sistema será encerrado e o programa será finalizado.

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    
    # Se o usário escolher uma opção inválida, o sistema exibirá uma mensagem de erro e solicitará que o usário selecione novamente a operação desejada.