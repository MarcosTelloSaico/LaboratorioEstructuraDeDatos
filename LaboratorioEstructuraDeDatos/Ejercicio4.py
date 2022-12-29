
##Ejercicio 4
##Escriba un programa recursivo y otro no recursivo para calcular n!.
# Compare los tiempos requeridos por los programas.
def recursivo1(n):
  if(n==0):
    return 1
  return n*recursivo1(n-1)
recursivo1(3)
## ---------------------------
def factorial1(n):
  resultado=1
  for i in range(n):
    resultado *=(i+1)
  return resultado
factorial1(3)