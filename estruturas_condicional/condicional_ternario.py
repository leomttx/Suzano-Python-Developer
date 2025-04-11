saldo = 200
saque = 100

status = "Saque realizado com sucesso" if saldo >= saque else "Saldo insuficiente"
print(status)