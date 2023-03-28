#Orden Numeros en una lista
def ordenar(lista, lon):
  if lon>1:
    for i in range(lon-1):
      if lista[i]>lista[i+1]:
        var=lista[i]
        lista[i]=lista[i+1]
        lista[i+1]=var
      ordenar(lista, lon -1)

l=[]
print('Ingrese cuatro numeros reales')
n1=float(input('Ingrese el primer numero:'))
l.append(n1)
n2=float(input('Ingrese el segundo numero:'))
l.append(n2)
n3=float(input('Ingrese el tercer numero:'))
l.append(n3)
n4=float(input('Ingrese el cuarto numero:'))
l.append(n4)
n5=float(input('Ingrese el quinto numero:'))
l.append(n5)

ordenar(l,len(l))
print('El numero menor es :', l[0])
print('El numero mayor es: ', l[len(l)-1])
count=0
acum=0
for i in l:
  count+=i
  acum+=1


promedio=count/acum
print('El promedio es: ', promedio)
#[50, 42, 23, 32, 1]

