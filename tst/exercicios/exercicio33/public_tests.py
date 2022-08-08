import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global maiores_final
        undertest = __import__(module)
        maiores_final = getattr(undertest, 'maiores_final', None)

    def test_semelhante_ao_da_prova_esq(self):
        fila = [12, 21, 35, 8, 12, 15]
        assert maiores_final(fila) == None
        assert fila == [12, 12, 15, 8, 21, 35]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
