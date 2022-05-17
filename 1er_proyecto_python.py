almacen = {1: ["pan",12]}
    

#---------Seccion del vendedor-----------
def agregar_producto():
    global almacen
    id = int(input("Ingrese el ID: "))
    nombre_producto = (input("Ingrese el nombre del producto: "))
    precio = (input("Ingrese el precio: "))
   

    almacen[id] = nombre_producto,precio
    print(almacen)

def delete(id):
    global almacen
    del(almacen[id])
    print("Eliminado")

def listar():
    global almacen
    for producto in almacen:
        print(
    """
        ID: {}
        Producto: {}
        Precio: {}
        
    """.format(producto,almacen[producto][0], almacen[producto][1]))


#---------Seccion del comrpador-----------


    



#---------Seccion de la maquina-----------
while True:
    print("""
    --------------------------------------
        Bienvenidos a mi tienda
    --------------------------------------      
    """)
    print("Menu \n\n 1.Agregar producto \n 2.Eliminar producto \n 3.Ver inventario \n 4.Salir")



    try:    
        opcion = int (input("\nSeleccione una opcion:-->"))

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            id = int(input("Ingrese el ID del producto"))
            delete(id) 
        elif opcion == 3: 
            listar()   
        elif opcion == 4:
            break     
        else:
            print("No esta esa opcion")   
    except:
        print("Por favor, ingresa un numero correcto! ")        

        