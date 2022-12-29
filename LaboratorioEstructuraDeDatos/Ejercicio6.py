##Ejercicio 6
## Un robot puede dar pasos de 1 o 2 metros.
## Escriba un programa para numerartodas las maneras en que el robot camina n metros.

def pasosRobot(n):
  if n == 1 or n == 2:
    return n
  return pasosRobot(n-1) + pasosRobot(n-2)
for i in range (1,p+1):
  print(pasosRobot(i))
p = int(input("Ingrese los metros que el robot caminará: "))
pasosRobot(8)
