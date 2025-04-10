# AND = Todos os termos precisam ser verdadeiros
# OR = Apenas um termo precisa ser verdadeiro
# NOT = Inverte o valor lógico
# XOR = Apenas um termo pode ser verdadeiro, não ambos

# Exemplo de uso dos operadores lógicos

a = True
b = False

# AND
print(a and b)  # False, pois b é False
print(a and a)  # True, pois ambos são True
print(b and b)  # False, pois ambos são False
print(a and (b or a))  # True, pois b or a é True e a é True

saldo = 1000
saque = 500


saque_autorizado = saldo >= saque and saldo > 0
print(f'True, pois saldo é maior que saque e maior que 0 -> {saque_autorizado}') 

saque_nao_autorizado = saldo < saque or saldo <= 0
print(f'False, pois saldo é maior que saque e maior que 0 -> {saque_nao_autorizado}')  