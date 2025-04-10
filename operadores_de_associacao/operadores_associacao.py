frutas = ["maçã", "banana", "laranja"]
precos = [3.50, 2.00, 4.00]
curso = "Curso de Python"

# Operador de associação
# O operador de associação é utilizado para verificar se um elemento está presente em uma coleção, como uma lista ou um dicionário.
# Ele retorna True se o elemento estiver presente e False caso contrário.
# O operador de associação é representado por "in" e "not in".


# Exemplo de uso do operador de associação
print("maçã" in frutas)  # True
print("uva" in frutas)  # False
print(2.00 in precos)  # True
print(5.00 not in precos)  # True
print("banana" not in frutas)  # False
print("laranja" in frutas)  # True
print("Curso" in curso)  # True
print("Python" in curso)  # True
print("Java" in curso)  # False
