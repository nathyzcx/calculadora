"""Calculadora com while"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_valido = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)  
        numeros_valido = True
    except:
        numeros_valido = None

    if numeros_valido is None:
        print('Um ou ambos os números são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operadores inválidos.')
        continue
            
    if len(operador) > 1:
        print('Apenas um operador.')
        continue

    print('Realizando sua conta...')

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    elif operador ==  '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    else:
        print('Nunca devia chegar aqui.')
            
    sair = input('Quer sair? ').lower().startswith('s')

    if sair is True:
        break
    
    