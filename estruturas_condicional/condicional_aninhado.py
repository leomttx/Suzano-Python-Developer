conta_normal = True
conta_especial = False

saldo = 1000.0
saque = 1700.0
cheque_especial = 500.0

if conta_normal:
    if saldo >= saque:
        saldo -= saque
        print(f'Saque de {saque} realizado com sucesso. Saldo atual: {saldo}')
    elif saque <= (saldo + cheque_especial):
        saldo -= saque
        cheque_especial -= abs(saldo)
        saldo = 0.0 
        print(f'Saque de {saque} realizado com sucesso. Saldo atual: {saldo} cheque especial utilizado no valor de {cheque_especial}')
    else:
        print('Saldo insuficiente')

elif conta_especial:
    if saldo >= saque:
        saldo -= saque
        print(f'Saque de {saque} realizado com sucesso. Saldo atual: {saldo}')
    elif saque <= (saldo + cheque_especial):
        saldo -= saque
        cheque_especial -= abs(saldo)
        saldo = 0.0
        print(f'Saque de {saque} realizado com sucesso. Saldo atual: {saldo} cheque especial utilizado no valor de {cheque_especial}')
    else:
        print('Saldo insuficiente')
else:
    print('Conta inválida')
