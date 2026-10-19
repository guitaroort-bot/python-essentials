
""" tarea del sombrero: Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4, y 5.

Tu tarea es:

escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1)
escribir una línea de código que elimine el último elemento de la lista (Paso 2)
escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
¿Listo para este desafío?
 """
# Lista de números en el sombrero   
hat_list = [1, 2, 3, 4, 5]

# Paso 1: Solicitar al usuario que reemplace el número central en la lista
hat_list[2] = int(input("Ingrese un número entero para reemplazar el número central (3): "))

# Paso 2: Eliminar el último elemento de la lista
del hat_list[-1]

# Paso 3: Imprimir la longitud de la lista existente
print("Longitud de la lista: ", len(hat_list))