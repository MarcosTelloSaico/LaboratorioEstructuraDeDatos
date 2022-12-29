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
