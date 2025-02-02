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