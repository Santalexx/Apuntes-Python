"""
print("Hola Mundo")
# Description: Este es un archivo de prueba para el curso de Python
print("Que más amigos")
a = 88
edad = 52
print(edad)

print("Vamos a hacer operaciones matematicas")
numero1 = int(input("Dame el primer número: "))
numero2 = int(input("Dame el segundo número: "))
suma = (numero1) + (numero2)
resta = (numero1) - (numero2)
multiplicacion = (numero1) * (numero2)
division = (numero1) / (numero2)
print("La suma de los números es: ", suma)
print("La resta de los números es: ", resta)
print("La multiplicacion de los números es: ", multiplicacion)
print("La division de los números es: ", division)


# Hacer un programa donde le preguntemos su nombre, el valor de sus tres productos y el valor total de sus tres productos

nombre = input("Dame tu nombre: ")
producto1 = float(input("Dame el valor del primer producto: "))
producto2 = float(input("Dame el valor del segundo producto: "))
producto3 = float(input("Dame el valor del tercer producto: "))
total = producto1 + producto2 + producto3
print("El total de tus productos es: ", "$", total)
metodoDePago = input("¿Con cuanto vas a pagar? ")
devueltas = float(metodoDePago) - total
print("Tu cambio es de: ", "$", devueltas)
print("Gracias por tu compra", nombre)
# Hacer un programa donde le pregunte al usuario que tabla de multiplicar mostrarle entre la tabla del 1 al 10

tabla = int(input("¿Qué tabla de multiplicar quieres ver? "))
print("Tabla del ", tabla)
print(tabla, "x 1 = ", tabla * 1)
print(tabla, "x 2 = ", tabla * 2)
print(tabla, "x 3 = ", tabla * 3)
print(tabla, "x 4 = ", tabla * 4)
print(tabla, "x 5 = ", tabla * 5)
print(tabla, "x 6 = ", tabla * 6)
print(tabla, "x 7 = ", tabla * 7)
print(tabla, "x 8 = ", tabla * 8)
print(tabla, "x 9 = ", tabla * 9)
print(tabla, "x 10 = ", tabla * 10)
"""

# Hacer un programa que le pregunte al usuario su nombre, su edad y su estatura y mostrarlo en pantalla

nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))
estatura = float(input("Dame tu estatura: "))
print("Tu nombre es: ", nombre)
print("Tu edad es: ", edad)
print("Tu estatura es: ", estatura)
print("Gracias por tu información")
