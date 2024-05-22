while True:
    # usuário informa os números
    x = str(input('Informe o primeiro número: ')).replace(',','.')
    y = str(input('Informe o segundo número: ')).replace(',','.')

    # converte para número decimais
    x = float(x)
    y = float (y)

    print('Operações Disponíveis: ')
    print('"+" para somar.')
    print('"-" para subtrair.')
    print('"*" para multiplicar.')
    print('"/" para dividir.')
    print('"%" para encontrar o resto da divisão.')
    print('"^" para exponenciar.')
    print('"!" para encontrar o fatorial.')
    

    op = input('Operação desejada: ')

    match op:
        case '+':
            print(f'A soma é: {x + y}.')
        case '-':
            print(f'A subtração é: {x - y}.')
        case '*':
            print(f'A multiplicação é: {x * y}.')
        case '/':
            print(f'A divisão é: {x / y}.')
        case '%':
            print(f'O resto da divisão é: {x % y}.')
        case '^':
            print(f'A exponecial é {x^y}')
        case '!':
            print(f'A fatoral é {x!}')
        case _:
            print('Operação inválida.')
            continue 