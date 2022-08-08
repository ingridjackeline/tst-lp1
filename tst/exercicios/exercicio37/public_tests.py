import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
insertion_sort = getattr(undertest, 'insertion_sort', None)

class PublicTests(unittest.TestCase):

   def test_exemplo(self):
      numeros = [6, 3, 7, 9, 1, 0]
      insertion_sort(numeros)
      assert numeros == [0, 1, 3, 6, 7, 9]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
