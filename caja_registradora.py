from math import prod
from os import remove
from pickle import APPEND


almacen = []

total = 0

print(""""--------------------------------------------------------
                Bienvenidos a mi tienda
 --------------------------------------------------------
                        Menu
""")

while True:
    print("""
    1. Añadir producto al almacen
    2. Retirar producto de almacen
    3. Ver almacen
    4. Añadir producto al carrito
    5. Retirar producto del carrito
    6. Cobrar
    7. Salir
    """)
    eleccion = input("Quiero la opcion: ")

    if eleccion == "1":
        producto = input ("Que producto desea agregar: ")
        if producto in almacen:
            print("Este produto ya se encuentra en el almacen")
        else:
            almacen.append(producto)
    elif eleccion == "2":
        producto = input ("Que producto desea eliminar: ")
        if producto not in almacen:
            print("Este producto no esta en el almacen")
        else: 
            almacen.remove(producto)
    elif eleccion == "3":
        for lista in almacen:
            print(lista)
    elif eleccion == "7":
        break
    else:
        print("No se elijio una opcion disponible")
        print()
            
   