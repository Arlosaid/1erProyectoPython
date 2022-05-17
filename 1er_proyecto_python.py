almacen = {"1": ["Pan",12]}
carrito = []
total = []
    

#---------Seccion del vendedor-----------
def agregar_producto():
    global almacen
    id = input("Ingrese el ID: ")
    nombre_producto = (input("Ingrese el nombre del producto: ").capitalize())
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


#---------Seccion del comprador-----------
def vendedor (): 
    global almacen
    respuesta_usuario = input ("Bienvenido, ingrese el ID del producto que desea comprar:-->")
    while respuesta_usuario != "salir":
        if respuesta_usuario in almacen:
            carrito.append(respuesta_usuario)
            carrito.append( almacen[respuesta_usuario][0])
            carrito.append( almacen[respuesta_usuario][1])
            respuesta_usuario = input("Muy bien, se ha agregado el producto a su carrito, desea algo mas? "
                                "(Escriba 'salir' para terminar su compra)")
        
        else:
            respuesta_usuario = input("Lo siento, no contamos con ese producto, desea algo mas?"
                                "(Escriba 'salir' para terminar su compra)")  
    print("Aqui estan tus productos del carrito: ", carrito)

    respuesta = input("Necesitas algo mas? (Escribe si/no").lower()


    if respuesta == "si":
        print("aqui esta lo que ordentaste ", carrito)
        vendedor()
        
     
     
                          

    


#---------Seccion de la maquina-----------
while True:
    print("""
    --------------------------------------
        Bienvenidos a mi tienda
    --------------------------------------      
    """)
    print("Menu \n\n 1.Agregar producto \n 2.Eliminar producto \n 3.Ver inventario \n 4.Comprar \n 5.Salir")



    try:    
        opcion = int (input("\nSeleccione una opcion:-->"))

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            id = input("Ingrese el ID del producto")
            delete(id) 
        elif opcion == 3: 
            listar()   
        elif opcion == 4:
            vendedor()
        elif opcion == 5:    
            break     
        else:
            print("No esta esa opcion")   
    except:
        print("Por favor, ingresa un numero correcto! ")        

