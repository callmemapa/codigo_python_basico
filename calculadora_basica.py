def run():
    print('BIENVENID@')
    numero1 = int(input('Ingrese número 1: '))
    numero2 = int(input('Ingrese número 2: '))
    menu = """
    Seleccione una de las siguientes opciones:
    1-) Suma
    2-) Resta
    3-) Multiplicación
    4-) División
    Escribe tu opción: """

    opcion = int(input(menu))
    if opcion == 1:
        resultado = int(numero1 + numero2)
    elif opcion == 2:
        resultado = int(numero1 - numero2)
    elif opcion == 3:
        resultado = int(numero1 * numero2)
    elif opcion == 4:
        resultado = int(numero1 / numero2)
    else:
        print('Ingrese una opción válida por favor.')

    print(resultado)


if __name__ == '__main__':
    run()