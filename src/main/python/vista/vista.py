from modelo.modelo import Articulo

class Menu():

    # Mostrar menu para preguntar con que va a trabajar (Art, Dep o St)
    def menu1(self):
        opcion = ''
        while opcion == '' or \
            (opcion != '1' and \
            opcion != '2' and \
            opcion != '3'):
            print('1: Articulo\n' +
                  '2: Depositos\n' +
                  '3: Stock\n')
            opcion = input('Opción: ')

        return opcion

    # Mostrar menu para preguntar qué quiere hacer (Alta, Baja, Modific)
    def menu2(self):
        opcion = ''
        while opcion == '' or \
            (opcion != '1' and \
            opcion != '2' and \
            opcion != '3'):
            print('1: Alta\n' +
                  '2: Baja\n' +
                  '3: Modificación\n')
            opcion = input('Opción: ')

        return opcion

    def altaArticulo(self):

        print('Ingrese el id de articulo\n(En blanco, genera automaticamente.)')
        idTemp = input('ID: ')

        print('Ingrese descripción del articulo.')
        descTemp = input('Desc: ')

        rsp = ''
        while rsp != 's' and rsp != 'n':
            print('Desea ingresar valores volumétricos?')
            rsp = input('(s/n)')

        if rsp == 's':
            altoTemp = input('Ingrese altura.')
            anchoTemp = input('Ingrese ancho.')
            largoTemp = input('Ingrese largo.')
        else:
            altoTemp = None
            anchoTemp = None
            largoTemp = None

        return(idTemp, descTemp, altoTemp, anchoTemp, largoTemp)
