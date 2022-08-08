import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
rotdir = getattr(undertest, 'rotdir', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        valores = [10, 20, 14, 17, 22, 9, 32]
        rotdir(valores)
        assert valores == [32, 10, 20, 14, 17, 22, 9]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
