#Old style %

nome = "Leo"
idade = 20
curso = "TADS"
profissao = "Programador"
salario = 4.000

print("Sou %s tenho %d anos faço %s trabalho como %s e recebo %f" % (nome, idade, curso, profissao, salario))

print()
#.format

print("Sou {} tenho {} anos faço {} trabalho como {} e recebo {:.3f}".format(nome, idade, curso, profissao, salario))

print()
#f string

print(f"Sou {nome} tenho {idade}")
