"""
conjunto = {"Mazda", "Renault", "Chevrolet"}
# conjunto.clear()
conjunto2 = conjunto.copy()
print(conjunto2)
"""

carros = {"Mazda", "Renault", "Chevrolet"}
colores = {"Rojo", "Azul", "Mazda", "Renault", "Chevrolet"}
# print(carros.difference(colores))
# carros.discard("Mazda")
# print(carros.intersection(colores))
# print(carros.issubset(colores))
# print(carros.issuperset(colores))

print(carros)
carros.pop(2)
print(carros)

# Hacer varios conjuntos de paises

paises = {"Colombia", "Perú", "Ecuador", "Venezuela"}
paises2 = {"Colombia", "Perú", "Ecuador", "Venezuela", "Chile", "Argentina"}

# Hacer una lista con los elementos de los conjuntos

paises = {"Colombia", "Perú", "Ecuador", "Venezuela"}
lista = list(paises)
print(lista)