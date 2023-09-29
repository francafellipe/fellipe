#faça um programa para determinar o número de digitos de um numero inteiro positivo informado
while True:
        escolha = int(input('1 - Iniciar programa :\n'
                            '2 - finalizar '))
        
        if escolha == 1 :
            num = int(input('Digite um número inteiro positivo: '))
            if num <= 0 :
                  print('O número deve ser maior que zero')
                  continue
            print(f'O número {num} tem {len(str(num))} digitos')
            continue

        else:
              break


