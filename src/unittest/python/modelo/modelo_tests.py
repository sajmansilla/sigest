from modelo.modelo import *
import unittest
from mock import *
#from modelo.dao import *

class TestArticulo(unittest.TestCase):
    def test_0_repr(self):

        artMock = Articulo()

        self.assertEqual(repr(artMock),'Articulo(%r, %r)'
                         %(artMock.id, artMock.descripcion))

    def test_1_find(self):

        artMock = Articulo()

        artMock.find = MagicMock(return_value = None)

        artMock.find('n')

        artMock.find.assert_called_once_with('n')

    def test_2_save(self):

        artMock = Articulo()

        artMock.save = MagicMock(return_value = None)

#       artMock.save.side_effect = DEFAULT

        artMock.save()

        artMock.save.assert_called_once_with()

    def test_3_setalto(self):

        artMock = Articulo()

        artMock.setAlto = MagicMock(return_value = None)

        artMock.setAlto(50)

        artMock.setAlto.assert_called_with(50)
#class TestDeposito(unittest.TestCase):


#class TestStock(unittest.TestCase):
