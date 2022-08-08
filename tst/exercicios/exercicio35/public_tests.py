import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

   @classmethod
   def setUpClass(cls):
       global remove_consecutivas
       undertest = __import__(module)
       remove_consecutivas = getattr(undertest, 'remove_consecutivas', None)
 
   def test_do_enunciado(self):
       lista1 = ['arara', 'tv',   'bacia']
       assert remove_consecutivas(lista1) == None
       assert lista1 == ['arara', 'tv',  'bacia']

   def test_do_enunciado_1(self):
       lista1 = ['arara', 'arroba',   'bacia']
       assert remove_consecutivas(lista1) == None
       assert lista1 == ['arara', 'bacia']
 
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__])) 
