import unittest
from meli.models import MeliProduct
from meli.meli import Meli


class MyProduct(MeliProduct):

    def __init__(self):
        super(MyProduct, self).__init__()
        self._other_attribute = 'test'


class TestMeli(unittest.TestCase):

    def test(self):
        p = MyProduct()
        p.title = 'Produto de teste'

        meli = Meli()
        meli.announce(p)


if __name__ == '__main__':
    unittest.main()