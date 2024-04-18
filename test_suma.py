import unittest
from suma import sumar
from suma import restar
from suma import multiplicar
from suma import dividir


class TestSumar(unittest.TestCase):
        
        def test_sumar(self):
          self.assertEqual(sumar(3,2), 5)
          self.assertEqual(sumar(-1,1), 0)
          self.assertEqual(sumar(-1,-1), -2)
          self.assertEqual(sumar(-1,0), -1)
        def test_restar(self):
          self.assertEqual(restar(2,1), 1)
          self.assertEqual(restar(2,-1), 3)
          self.assertEqual(restar(-2,-1), -1)
          self.assertEqual(restar(2,0), 2)
        def test_multiplicar(self):  
          self.assertEqual(multiplicar(2,1), 2)
          self.assertEqual(multiplicar(2,-1), -2)
          self.assertEqual(multiplicar(-2,-1), 2)
          self.assertEqual(multiplicar(-2,0), 0)

        def test_dividir(self):  
          self.assertEqual(dividir(2,1), {'resultado': 'el resultado es 2.0'} )
          self.assertEqual(dividir(2,-1), {'resultado': 'el resultado es -2.0'})
          self.assertEqual(dividir(-2,-1), {'resultado': 'el resultado es 2.0'})


          self.assertEqual(dividir(2,0),{"message":"error no se puede dividir por 0"} )



if __name__=='__main__':
      unittest.main()
    
    