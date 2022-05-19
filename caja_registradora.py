almacen = {"1": ["Pan",12],"2": ["Leche",25],"3": ["Agua",26],"4": ["Manzana",5],"5": ["Naranja",7]}
carrito = []
total = []
    

#---------Seccion del vendedor-----------
def agregar_producto():
    global almacen
    id = (input("Ingrese el ID del producto que desea registrar:-->"))
    
    if id  in almacen:
        print("Ese ID ya esta registrado")
    
    else:
        nombre_producto = (input("Ingrese el nombre del producto:-->").capitalize())
        precio = int(input("Ingrese el precio: "))
        almacen[id] = nombre_producto,precio
        print("Se registro exitosamente el producto")
   
    respuesta = input("Desea agregar otro producto al almacen? si/no -->").lower()
    if respuesta == "si":
        agregar_producto()


def borrar(id):
    global almacen
    id = (input("Ingrese el ID del producto que desa eliminar:-->"))
    if id  in almacen:
       print("\nSe elimino el producto del almacen\n")
       del(almacen[id])

    else:         
        print("\nEse producto no se encuentra en almacen\n")
    
    respuesta = input("Desea quitar otro producto al almacen? si/no-->").lower()
    if respuesta == "si":
        borrar(id)       


def listar():
    global almacen
    print("\n-------------Productos en el inventario-------------\n")
    for producto in almacen:
        print(
    """ID: {}
        Producto: {}
        Precio: {} """.format(producto,almacen[producto][0], almacen[producto][1]))



#---------Seccion del comprador-----------
def vendedor ():
    comprar = input("\nAgregue el ID del producto que desea comprar-->\n ")

    if comprar in almacen:
        carrito.append(comprar)
        print(carrito)
    
    else:
        print("No contamos con este producto, lo siento\n")
            
    comp_respuesta = input("Desea comprar otro producto? si/no-->")
    if comp_respuesta == "si":
        vendedor()


def eliminar_prod ():
    eliminar = input("\nQue producto desea eliminar:-->\n")
    
    if eliminar in carrito:
        for prod_elim in range(len(carrito)-1,-1,-1):
            if carrito[prod_elim] == eliminar:
                carrito.pop(prod_elim)
        
                print("\nSe elimino el producto\n")
                print(carrito)
    
    else:
        print("\nNo cuenta con este producto en su carrito\n")
    
    elim_respuesta = ("Desea eliminar otro producto? si/no-->")
    if elim_respuesta == "si":
        eliminar_prod()


def pagar ():
    for items in carrito:
        total.append(almacen[items][1])
        total_pagar = sum(total)
    print("\nTotal a pagar", total_pagar," pesos\n")
    
        
                      

    
#---------Seccion de la maquina-----------
while True:
    print("""
    --------------------------------------
        Bienvenidos a mi tienda
    --------------------------------------      
    """)
    print("Menu \n\n 1.Agregar producto \n 2.Eliminar producto \n 3.Ver inventario \n 4.Comprar  \n 5.Eliminar producto del carrito \n 6.Pagar \n 7.Salir")



    try:    
        opcion = int (input("\nSeleccione una opcion:-->"))

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            borrar(id) 
        elif opcion == 3: 
            listar()   
        elif opcion == 4:
            vendedor()
        elif opcion == 5:
            eliminar_prod()    
        elif opcion == 6:
            pagar()
                
        elif opcion == 7:    
            break     
        else:
            print("No esta esa opcion")   
    except:
        print("Por favor, ingresa un numero correcto! ")        

