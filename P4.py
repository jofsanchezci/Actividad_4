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

max_value = max(l)
min_value = min(l)
average = sum(l) / len(l)

print(f"El valor maximo es: {max_value}")
print(f"El valor minimo es: {min_value}")
print(f"El promedio es: {average}")


