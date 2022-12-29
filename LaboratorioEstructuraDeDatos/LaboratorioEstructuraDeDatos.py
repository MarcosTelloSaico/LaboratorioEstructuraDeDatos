##Ejercicio 1 
## Implemente el siguiente algoritmo como un programa para desordenar. 
## desordena(a, n){ for i = 1 to n − 1 swap(ai,arand(i,n))
import random
def desordena(a,n):
  for i in range(n):
    ra=random.randint(i,n-1)
    a[i],a[ra]=a[ra],a[i]
s=[1,3,5,7,8,9]
desordena(s,len(s))
print(s)

## Ejercicio 2
## Corra el algoritmo anterior “desordena” (del ejercicio 1) 
## muchas veces para la misma sucesión de entrada. 
#  ¿Como puede analizarse la salida para determinar si es verdaderamente “aleatorio”?
import random
def desordena(a,n,i):
  if i<n:
    ra=random.randint(i,n-1)
    a[i],a[ra]=a[ra],a[i]
    desordena(a,len(a),i+1)
s=[1,3,5,7,8,9]
desordena(s,len(s),0)
print(s)

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


##Ejercicio 6
## Un robot puede dar pasos de 1 o 2 metros.
## Escriba un programa para numerartodas las maneras en que el robot camina n metros.

def pasos_robot(n):
  if n == 1 or n == 2:
    return n
  return pasos_robot(n-1) + pasos_robot(n-2)
p = int(input("Ingrese los metros que el robot caminará: "))
for i in range (1,p+1):
  print(pasos_robot(i))

##Ejercicio 7
## Un robot puede dar pasos de 1, 2 o 3 metros.
## Escriba un programa para numerar todas las maneras en que el robot camina n metros.
def robot(n):
  if n == 1 or n == 2:
    return n
  elif n ==3:
    return n+1
  return robot(n-1) + robot(n-2) + robot(n-3)
p = int(input("Ingrese los metros que el robot caminará: "))
for i in range (1,p+1):
  print(pasos_robot(i))
print(pasos_robot(8))

##Ejercicio 8
## Implemente un programa recursivo que calcule la potencia de un nu mero elevado a otro. 
## Sabemos que 2n = 2n/2. 2n/2 donde n es un nro par; y 2n = 2(n-1)/2. 2(n-1)/2.2 si n es impar
def potencia(a,b):
  if b==1:
    return a
  else:
    if b%2 == 0:
      pot=potencia(a,int(b/a))
      return pot*pot
    else:
      return a*potencia(a,b-1)
potencia(8,9)

##Ejercicio 9
## Implemente un programa recursivo que sume dos números a + b. 
## Considera que la suma a+b = a + 1 + 1 + ...+ 1 (b veces)
def sumaRecursiva(a,b):
  if b==0:
    return a
  else:
    return sumaRecursiva(a,b-1)+1
sumaRecursiva(8,9)

##Ejercicio 10
##     ¿Cuáles son las principales ventajas de la programación recursiva en Python?
##  Una tarea compleja se puede dividir en subproblemas más simples mediante la recursividad. 
##  Esto facilita el abordaje de la programación de una forma mucho más flexible y sencilla.