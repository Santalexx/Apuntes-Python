frutas = ('fresas', 'papaya', 'naranja')
frutas2 = ['fresas', 'papaya', 'naranja']

print(frutas)

print(type(frutas))
print(type(frutas2))

print(frutas.count('fresas'))
print(frutas.index('fresas'))

temporal = list(frutas)

print(frutas)
print(temporal)

temporal.pop(2)
print(temporal)

frutas = tuple(temporal)
print(frutas)

print(frutas)

fruits = ('apple', 'banana', 'cherry', 'dates', 'elderberry', 'fig', 'grape')
(x, *y, z) = fruits
print(y)

# Hacer una lista y agregar varios elementos a cada uno

frutas = ['fresas', 'papaya', 'naranja']
frutas.append('manzana')
frutas.append('pera')
frutas.append('uva')
print(frutas)
