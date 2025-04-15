#O comando while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira.
#É útil quando não sabemos o número exato de iterações que precisamos fazer.
#O loop while continua até que a condição se torne falsa.
#É importante garantir que a condição eventualmente se torne falsa, para evitar loops infinitos.
#O loop while pode ser controlado com as instruções break e continue, semelhantes ao loop for.
#A instrução break encerra o loop imediatamente, enquanto a instrução continue pula para a próxima iteração.

opcao = -1

while opcao != 0:
    print('Menu de Opções')
    print('1 - Adicionar')
    print('2 - Remover')
    print('3 - Alterar')
    print('4 - Listar')
    print('0 - Sair')
    opcao = int(input('Escolha uma opção: '))
    print()
    if opcao == 1:
        print('Adicionando...')
    elif opcao == 2:
        print('Removendo...')
    elif opcao == 3:
        print('Alterando...')
    elif opcao == 4:
        print('Listando...')
    elif opcao == 0:
        print('Saindo...')
    else:
        print('Opção inválida!')

