saldo = 100
valor_deposito = 50
valor_saque = 50

# Operador de identidade
# O operador de identidade é utilizado para verificar se duas variáveis são o mesmo objeto na memória.
# Ele retorna True se as variáveis referenciam o mesmo objeto e False caso contrário.
# O operador de identidade é representado por "is" e "is not".

# Exemplo de uso do operador de identidade
print("Saldo é o mesmo objeto que valor_deposito?", saldo is valor_deposito)  # False
print("Saldo é o mesmo objeto que valor_saque?", saldo is valor_saque)  # False
print("Valor de saque é o mesmo objeto que valor_deposito?", valor_saque is valor_deposito)  # True