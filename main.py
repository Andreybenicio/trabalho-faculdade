def dimensoesObjeto():
    while True:
        try:
            comprimento = int(input('Digite o comprimento do objeto (em cm): '))
            largura = int(input('Digite a largura do objeto (em cm): '))
            altura = int(input('Digite a altura do objeto (em cm): '))

            volume = altura * largura * comprimento
            if volume < 1000:
                return 10
            elif 1000 <= volume < 10000:
                return 20
            elif 10000 <= volume < 30000:
                return 30
            elif 30000 <= volume < 100000:
                return 50
            else:
                print('O volume do objeto é (cm³): {} \n '
                      'Não aceitamos objetos com dimensões tão grandes! Digite novamente.'.format(volume))
                continue
        except ValueError:
            print('Você digitou alguma dimensão com valor não numérico \n'
                  'Digite as dimensões desejadas novamente.')
            continue


def pesoObjeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto (kg): '))
            if peso <= 0.1:
                return 1
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            else:
                print('Não aceitamos objetos tão pesados! \n'
                      'Digite apenas pesos aceitos (kg)')
                continue
        except ValueError:
            print('Você digitou um valor não numérico \n'
                  'Digite o peso desejado novamente')
            continue


def rotaObjeto():
    print('Rota \n'
          'RS - De Rio de Janeiro até São Paulo \n'
          'SR - De São Paulo até Rio de Janeiro \n'
          'BS - De Brasília até São Paulo \n'
          'SB - De São Paulo até Brasília \n'
          'BR - De Brasília até Rio de Janeiro \n'
          'RB - De Rio de Janeiro até Brasília')

    while True:
        rota = input('Digite a rota desejada: ').upper()
        if rota == 'RS' or rota == 'SR':
           return 1
        elif rota == 'BS' or rota == 'SB':
            return 1.2
        elif  rota == 'BR' or rota == 'RB':
            return 1.5
        else:
            print('Você digitou uma rota que não existe \n'
                  'Digite a rota novamente')



#programa principal
print('-----Bem-vindo a companhia de Logistica Andrey Benicio de Souza-----')
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensoes * peso * rota
print('Total a pagar (R$): {} (Dimensões: {} * Peso: {} * Rota: {})'.format(total, dimensoes, peso, rota))