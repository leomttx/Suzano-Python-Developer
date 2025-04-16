palavra = 'leOnArDo'

print(palavra.upper())

print(palavra.lower())

print(palavra.title())

print()

texto = '  Olá mundo      '
print(texto + '.')
print(texto.strip() + '.') #removeu os espaços em branco
print(texto.lstrip() + '.') #removeu os espaços em branco da esquerda
print(texto.rstrip() + '.') #removeu os espaços em branco da direita

print()

#Cetralização
menu = "MENU"
print("####" + menu + "####") 
print(menu.center(12))
print(menu.center(12, "#"))

print()

#Inclusão
python = "Python"
print("P-y-t-h-o-n")
print('-'.join(python))


