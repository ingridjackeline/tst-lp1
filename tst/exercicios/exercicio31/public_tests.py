import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global uniao_listas
        undertest = __import__(module)
        uniao_listas = getattr(undertest, 'uniao_listas', None)

    def test_exemplo(self):
        l1 = [2,1,3,4]
        l2 = [2]
        assert uniao_listas(l1,l2) == None
        assert l1 == [2,1,3,4]
        assert l2 == [2]

        l1 = [1,3,4]
        l2 = [4]
        assert uniao_listas(l1,l2) == None
        assert l1 == [1,3,4]
        assert l2 == [4]

        l1 = [2,4,1]
        l2 = [6,7,91]
        uniao_listas(l1,l2)
        assert l1 == [2,4,1,6,7,91]
        assert l2 == [6,7,91]
 

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
