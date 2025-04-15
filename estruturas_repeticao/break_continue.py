#Break é uma instrução que interrompe o loop, enquanto continue pula para a próxima iteração do loop.
#Break é útil quando queremos sair do loop antes que a condição se torne falsa, enquanto continue é útil quando queremos pular uma iteração específica.
#O loop while pode ser controlado com as instruções break e continue, semelhantes ao loop for.
#A instrução break encerra o loop imediatamente, enquanto a instrução continue pula para a próxima iteração.

while True:
    numero = int(input('Digite um número:'))
    if numero == 0:
        break
    elif numero == 1:
        continue
    print(f'Você digitou o número {numero}')

print('Fim do programa')

for i in range(10):
    if i % 2 == 0: # se o número for par, pula para a próxima iteração
        continue
    print(i, end=' ') # imprime apenas os números ímpares
print('Fim do programa')
