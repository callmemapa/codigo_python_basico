menu = """
Bienvenid@, ingrese un número para mostrar la tabla de este número
Escribe tu opción: """


def multiplicador(num):
    print('Tabla del ' + str(num) + ':')
    for i in range(1, 11):
        print(str(num) + ' * ' + str(i) + ' = ' + str(num*i))


def run():
    opcion = int(input(menu))
    multiplicador(opcion)


if __name__ == '__main__':
    run()