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
