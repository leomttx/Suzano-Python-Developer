nome = "Leonardo"
idade = 20

print(nome, idade)

sobrenome, idade = "Silva", 21 # Atribuição múltipla
# O Python permite atribuir valores a várias variáveis em uma única linha.

print(f"Nome: {nome}, Sobrenome: {sobrenome}, Idade: {idade}") # Formatação de strings

print(sobrenome, idade)

limite_saque_diario = 1000 # padrão snake_case

ESTADOS_BRASILEIROS = ["SP", "RJ", "MG", "ES"] # Formato padrão para constantes
# O padrão é usar letras maiúsculas e separadas por underline para constantes
# Isso ajuda a identificar que o valor não deve ser alterado durante a execução do programa.

print(ESTADOS_BRASILEIROS)