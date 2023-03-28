#Conversión de temparaturas.
c=float(input('Ingrese la temperatura en Grados Celcius: '))
f=((9/5)*c) + 32
r=((c*1.8)+491.67)
k=c+273.15
print(c, 'es equivalente a', f,'Grados Fahrenheit')
print(c, 'es equivalente a', r,'Grados Rankine')
print(c, 'es equivalente a', k,'Grados Kelvin')
