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