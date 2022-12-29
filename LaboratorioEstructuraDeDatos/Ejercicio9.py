##Ejercicio 9
## Implemente un programa recursivo que sume dos números a + b. 
## Considera que la suma a+b = a + 1 + 1 + ...+ 1 (b veces)
def sumaRecursiva(a,b):
  if b==0:
    return a
  else:
    return sumaRecursiva(a,b-1)+1
sumaRecursiva(8,9)

