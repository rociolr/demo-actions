import unittest
from suma import sumar
from suma import restar
from suma import multiplicar
from suma import dividir


class TestSumar(unittest.TestCase):
        
        def test_sumar(self):
          #comprobar la función suma de dos numeros positivos
          self.assertEqual(sumar(3,2), 5)
          #comprobar la función suma de dos numeros uno positivo y otro negativo
          self.assertEqual(sumar(-1,1), 0)
          #comprobar la función suma de dos numeros negativos
          self.assertEqual(sumar(-1,-1), -2)
          #comprobar la función suma de dos numeros con uno de ellos que sea 0
          self.assertEqual(sumar(-1,0), -1)
        def test_restar(self):
          #comprobar la función restar de dos números positivos
          self.assertEqual(restar(2,1), 1)
          #comprobar la función restar de dos números uno positivo y otro negativo
          self.assertEqual(restar(2,-1), 3)
          #comprobar la función restar de dos números negativos
          self.assertEqual(restar(-2,-1), -1)
          #comprobar la función restar de dos números y uno de ellos sea 0
          self.assertEqual(restar(2,0), 2)
        def test_multiplicar(self):  
          #comprobar la función multiplicar de dos números positivos
          self.assertEqual(multiplicar(2,1), 2)
          #comprobar la función multiplicar de dos números y uno sea positivo y el otro negativo
          self.assertEqual(multiplicar(2,-1), -2)
          #comprobar la función multiplicar de dos números negativos
          self.assertEqual(multiplicar(-2,-1), 2)
          #comprobar la función multiplicar de dos números y uno de ellos sea 0
          self.assertEqual(multiplicar(-2,0), 0)

        def test_dividir(self):  
           #comprobar la función dividir de dos números positivos
          self.assertEqual(dividir(2,1), {'resultado': 'el resultado es 2.0'} )
           #comprobar la función dividir de dos números y uno sea negativo y otro positivo
          self.assertEqual(dividir(2,-1), {'resultado': 'el resultado es -2.0'})
           #comprobar la función dividir de dos números negativos
          self.assertEqual(dividir(-2,-1), {'resultado': 'el resultado es 2.0'})
           #comprobar la función dividir de dos números y el segundo sea 0


          self.assertEqual(dividir(2,0),{"message":"error no se puede dividir por 0"} )



if __name__=='__main__':
      unittest.main()
    
    