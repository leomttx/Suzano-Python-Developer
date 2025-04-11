MATRICULA = "4109114" 
VISITANTE = "Visitante"

entrada = str(input("Digite sua matricula: "))
if entrada == MATRICULA:
    print("Matricula correta")
else: 
    print("Matricula incorreta")

if entrada == MATRICULA:
    print("Matricula correta")
elif entrada == VISITANTE:
    print("Bem-vindo visitante")
else:
    print("Matricula incorreta")