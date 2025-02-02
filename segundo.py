"""
frutas = ['naranja', 'papaya', 'pera', 'manzana']
tamaño = len(frutas)
print(frutas)
frutas.append('manzana')
print(frutas)
frutas[1]='mango'
print(frutas)
frutas.insert(2, 'uva')
print(frutas)

frutas.clear()
print(frutas)
del frutas
print(frutas)

frutas2 = frutas.copy()
print(frutas2)
frutas2.append('durazno')
print(frutas)
print(frutas2)
# frutas3 = frutas
# frutas3.append('sandía')
# print(frutas3)
print(frutas)
cantidad = frutas.count('manzana')
print(cantidad)
carros= ['toyota', 'nissan', 'ford']
frutas.extend(carros)
print(frutas)

print(frutas.index('ford'))
frutas.pop()
print(frutas)
frutas.pop(2)
print(frutas)
frutas.remove('naranja')
print(frutas)
frutas.remove('manzana')
print(frutas)
frutas.reverse()
print(frutas)
frutas.sort()
print(frutas)
print(frutas[1:3])

lista1 = []
precio = int(input("Ingrese el precio: "))
lista1.append(precio)
print(lista1)
nombre = input("Ingrese el nombre: ")
lista1.append(nombre)
print(lista1)

palabra = 'Hola Mundo'
print(palabra[0])
print(len(palabra))
print(palabra[2:6])
"""

# Hacer una lista, tupla y diccionario con los siguientes elementos: 1, 2, 3, 4, 5

lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
diccionario = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5}

# Hacer una lista con los elementos de la tupla

lista2 = list(tupla)
print(lista2)