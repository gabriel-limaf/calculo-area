"""
Calculo de área em Python by Gabriel Lima
"""
print('Bem-vindo a calculadora de área em Python!')


def inicio():
    while True:
        figura = int(input('Qual figura deseja calcular a área?\n'
                           'Quadrado: Digite 1\n'
                           'Triangulo: Digite 2\n'
                           'Círculo: Digite 3\n'
                           'Losango: Digite 4\n'
                           'Trapézio: Digite 5\n'
                           'Encerrar Programa: Digite 6\n'))
        if figura not in [1, 2, 3, 4, 5, 6]:
            print("Escolha um valor válido \n")
            continue
        elif figura == 1:
            area_quadrado()
        elif figura == 2:
            area_triangulo()
        elif figura == 3:
            area_circulo()
        elif figura == 4:
            area_losango()
        elif figura == 5:
            area_trapezio()
        elif figura == 6:
            break


def area_quadrado():
    um = input('Qual a unidade de medida?: ')
    base = float(input('Qual o comprimento da base do quadrado?: '))
    alt = float(input('Qual o comprimento da altura do quadrado?: '))
    area = base * alt
    print(f'A área do quadrado é de {area} {um}²\n')


def area_triangulo():
    um = input('Qual a unidade de medida?: ')
    base = float(input('Qual o comprimento da base do triangulo?: '))
    alt = float(input('Qual o comprimento da altura do tringulo?: '))
    area = (base * alt) / 2
    print(f'A área do triangulo é de {area} {um}²\n')


def area_circulo():
    um = input('Qual a unidade de medida?: ')
    raio = float(input('Qual o raio do circulo?:'))
    area = 3.14 * raio * raio
    print(f'A área do circulo é de {area} {um}²\n')


def area_losango():
    um = input('Qual a unidade de medida?: ')
    d1 = float(input('Qual o comprimento da diagonal 1?: '))
    d2 = float(input('Qual o comprimento da diagonal 2?: '))
    area = (d1 * d2) / 2
    print(f'A área do losango é de {area} {um}²\n')


def area_trapezio():
    um = input('Qual a unidade de medida?: ')
    b1 = float(input('Qual o comprimento da base maior?: '))
    b2 = float(input('Qual o comprimento da base menor?: '))
    alt = float(input('Qual o comprimento da altura do trapezio?: '))
    area = ((b1 + b2) * alt) / 2
    print(f'A área do trapezio é de {area} {um}²\n')


inicio()
