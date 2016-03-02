from modelo.modelo import Articulo, Deposito, Stock
from vista.vista import Menu

class Control():
    menus = Menu()

    opcObj = menus.menu1()

    opcionesObj = {'1': Articulo, '2': Deposito,
                '3': Stock}

    obj = opcionesObj[opcObj]()
    #print(repr(obj))

    opcAct = menus.menu2()

    opcionesAct = {'1': alta+menus.opcionesObj[opcObj](), '2': baja,
                '3': modif}

    #print(opciones[opcion])

    (id, desc, alto, ancho, largo) = menus.opcionesAct[opcAct]

    print(id, desc, alto, ancho, largo)

