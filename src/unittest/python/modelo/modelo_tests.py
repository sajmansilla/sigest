from modelo.modelo import *
import unittest
import mock

class TestArticulo(unittest.TestCase):
    # Declarar variables internas para los tests
    idArt = 'n'
    descArt = 'n'

    artMock = Articulo()
    artMock.id = idArt
    artMock.descripcion = descArt

    artMockExcept = Articulo()
    artMockExcept.id = idArt
    artMockExcept.descripcion = descArt

    def test0_find_mock(self):
        articulo = mock.create_autospec(Articulo)
        articulo.save.return_value = 'El Articulo se inserto correctamente.'
        expect = 'El Articulo se inserto correctamente.'
        result = articulo.save()
        self.assertEqual(expect, result)

    def test1_save_try(self): # Hace el test del metodo save de Articulo
        expected = 'El Articulo se inserto correctamente.'
        result = self.artMock.save()
        self.assertEqual(result, expected)

    def test2_save_except(self): # Hace el test del metodo save de Articulo
        expected = 'Hubo un error en la insercion.'
        result = self.artMockExcept.save()
        self.assertEqual(result, expected)

    def test3_find(self): # Hace el test del metodo find de Articulo
        expected = Articulo()
        expected.id = 'n'
        expected.descripcion = 'n'
        result = self.artMock.find(self.idArt)
        self.assertEqual(repr(result), repr(expected))

    def test3_notfind(self):
        self.assertEqual(self.artMock.find('x'),'No se encontro')

    def test4_dlt(self): # Hace el test del metodo dlt de Articulo
        self.assertEqual(self.artMock.dlt(), "El Articulo se elimino " +
                         "correctamente.")

    def test4_dlt_except(self): # Test de except metodo dlt [Articulo]
        expected = 'Error eliminando.'
        result = self.artMockExcept.dlt()
        self.assertEqual(result,expected)

    def test5_repr(self): # Hace el test del metodo repr de Articulo
        self.assertEqual(repr(self.artMock),'Articulo(%r, %r)'
                         %(self.artMock.id, self.artMock.descripcion))

class TestDeposito(unittest.TestCase):
    #Definir variables internas
    idDep = 'id deposito'
    descripcionDep = 'descrip deposito'

    depMock = Deposito()
    depMock.id = idDep
    depMock.descripcion = descripcionDep
    depMock.texto = 'Texto Mock'

    depMockExcept = Deposito()
    depMockExcept.id = idDep
    depMockExcept.descripcion = descripcionDep
    depMockExcept.texto = 'Texto Mock Except'

    def test1_save_try(self):
        expected = 'El Deposito se inserto correctamente.'
        result = self.depMock.save()
        self.assertEqual(result, expected)

    def test2_save_except(self):
        expected = 'Error insertando el Deposito.'
        result = self.depMockExcept.save()
        self.assertEqual(result, expected)

    def test3_find(self):
        expected = Deposito()
        expected.id = self.idDep
        expected.descripcion = self.descripcionDep
        expected.texto = 'Texto Mock'
        result = self.depMock.find(self.idDep)
        self.assertEqual(repr(result), repr(expected))

    def test3_notfind(self):
        self.assertEqual(self.depMock.find('n'),'No se encontro el deposito')

    def test4_dlt(self): # Hace el test del metodo dlt de Deposito
        self.assertEqual(self.depMock.dlt(), "El Deposito se elimino " +
                         "correctamente.")

    def test4_dlt_except(self): # Test de except metodo dlt [Deposito]
        expected = 'Error eliminando el Deposito.'
        result = self.depMockExcept.dlt()
        self.assertEqual(result,expected)

    def test5_repr(self): # Hace el test del metodo repr de Deposito
        expected ='Deposito(%r,%r)'%(self.depMock.id, self.depMock.descripcion)
        result = repr(self.depMock)
        self.assertEqual(result, expected)

class TestStock(unittest.TestCase):
    # Declarar variables internas para los tests
    idArt = 'nArt'
    idDep = 'nDep'
    cantid = 5

    stkMock = Stock(idArt, idDep, cantid)

    artMock = Articulo()
    artMock.id = idArt
    artMock.descripcion = 'Mock stock'

    depMock = Deposito()
    depMock.id = idDep
    depMock.descripcion = 'Mock stock'
    depMock.texto = 'Texto Mock'

    def test1_save(self): # No puede guardar porque no existe Dep o Art.
        expected = 'Error registrando el stock. Excepcion de integridad.'
        result = self.stkMock.save()
        self.assertEqual(result, expected)

    def test2_findDep(self):
        expected = 'Deposito'
        result = self.stkMock.find('',self.idDep)
        self.assertEqual(result, expected)

    def test100_repr(self):
        expected = 'Stock del Articulo(%r) en Deposito(%r):'%(self.idArt,
                                                              self.idDep)
        result = repr(self.stkMock)
