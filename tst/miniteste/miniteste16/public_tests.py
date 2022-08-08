import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class AcceptanceTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global vacina_idosos
        undertest = __import__(module)
        vacina_idosos = getattr(undertest, 'vacina_idosos', None)

    def test_exemplo(self):
        fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
        assert vacina_idosos(fila) == None
        assert fila == [67, 61, 63, 75, 25, 33, 35, 8, 12, 15, 22, 30, 34]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
