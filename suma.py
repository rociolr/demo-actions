def sumar(a, b):
    return a + b

if __name__=="__main__":
    print(sumar(5,3))

def restar(a, b):
    return a - b

if __name__=="__main__":
    print(restar(2,-1))    

def multiplicar(a, b):
    return a * b

if __name__=="__main__":
    print(multiplicar(5,3))    


def dividir(a, b):
   # return a / b
 if b==0:
     return {"message":"error no se puede dividir por 0"}
 else:
      resultado=a/b
      return {"resultado": f"el resultado es {resultado}"}
              
if __name__=="__main__":
    print(dividir(5,3))    
