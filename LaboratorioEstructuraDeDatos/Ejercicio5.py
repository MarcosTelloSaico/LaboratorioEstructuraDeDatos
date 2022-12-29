##Ejercicio 5
## Escriba un programa recursivo y otro no recursivo para calcular la sucesión deFibonacci. 
## Compare los tiempos requeridos por los programas

def fibonacci(n):
  if(n == 0):
    return 0
  else:
    a = 0
    b = 1
    for i in range (1,n):
      c = (a+b)
      a = b
      b = c
      return b
for i in range(5):
  print(fibonacci(i))

##----------------------------------
def fibonacci_recursivo(n):
  if n == 0 or n == 1:
    return n
  else:
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
  fibonacci_recursivo(8)
print(fibonacci_recursivo(8))

