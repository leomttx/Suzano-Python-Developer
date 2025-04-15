# o laço for permite iterar sobre uma sequência (como uma lista, tupla ou string) ou um objeto iterável
# o laço for é mais utilizado quando sabemos o número de iterações que queremos fazer

texto = input('Digite um texto: ')
vogais = 'AEIOU'

for letra in texto:
    if letra.upper() in vogais:
        print(letra)

print('Fim do programa') 

# Função built-in range()
# range() é uma função que gera uma sequência de números inteiros, muito utilizada em laços for
# range(início, fim, passo)
# início: valor inicial (inclusivo)
# fim: valor final (exclusivo)
# passo: valor do incremento (padrão é 1)
# range(5) gera uma sequência de 0 a 4 (5 não é incluído)

print(range(5))
print(list(range(5))) # converte o range em uma lista
print(list(range(1, 10))) # gera uma lista de 1 a 9
print(list(range(1, 10, 2))) # gera uma lista de 1 a 9 com passo 2
print(list(range(10, 0, -1))) # gera uma lista de 10 a 1 com passo -1

for i in range(5):
    print(i+5) # imprime os números de 0 a 4