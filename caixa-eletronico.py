# Saldo inicial da conta
saldo = 1000 

while True:

    # Opções do menu:
    print("\nCaixa Eletrônico")
    print("1- Verificar saldo")
    print("2- Depositar dinheiro")
    print("3- Sacar dinheiro")
    print("4- Sair")

    
    opção = str(input("Escolha o número de 1-4: "))


    # PARTE DA VIZUALIZAÇÃO DE SALDO
    if opção == "1":
        print("{:.2f} de saldo".format(saldo))


    # PARTE DO DEPÓSITO
    elif opção == "2":
        
        while True:
            dep = float(input("Qual o valor do depósito? R$: ")) # dep é o valor do depósito
            if dep < 0:
                print("Valor inválido, Tente novamente!")
            else:
                saldo += dep # O valor do depósito é somado ao saldo
                print("Depósito de {} realizado com sucesso! Seu saldo atual é de: {:.2f}! ".format(dep, saldo))
                break
            

    # PARTE DO SAQUE
    elif opção == "3":
        while True:

            saque = float(input("Quanto vai sacar? R$ "))
            if saque > saldo:
                print("Valor inválido. Tente novamente!")

            elif saque < 0:
                print("Valor inválido. Tente novamente!")

            else:
                saldo -= saque
                print("Saldo atual: ", saldo)
                break  

    
    # SAÍDA
    elif opção == "4":
        print("Operação finalizada")
        break
    else:
        print("Valor inválido")
        


