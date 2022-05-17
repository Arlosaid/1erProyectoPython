almacen = {"1": ["Pan",12],"2": ["Leche",25]}
carrito = []
total = []
    

#---------Seccion del vendedor-----------
def agregar_producto():
    global almacen
    id = (input("Ingrese el ID: "))
    nombre_producto = (input("Ingrese el nombre del producto: ").capitalize())
    precio = int(input("Ingrese el precio: "))
   

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
    comprar = input("Agregue el ID del producto que desea comprar ")

    if comprar in almacen:
        carrito.append(comprar)
        
       
        
        print(carrito)

def eliminar_prod ():
    eliminar = input("Que producto desea eliminar: ")
    for i in range(len(carrito)-1,-1,-1):
        if carrito[i] == eliminar:
         carrito.pop(i)
        
        print("\nSe elimino el producto\n")
        print(carrito)

def pagar ():
    for items in carrito:
        total.append(almacen[items][1])
        total_pagar = sum(total)
    print("Total a pagar", total_pagar)

        
                      

    
#---------Seccion de la maquina-----------
while True:
    print("""
    --------------------------------------
        Bienvenidos a mi tienda
    --------------------------------------      
    """)
    print("Menu \n\n 1.Agregar producto \n 2.Eliminar producto \n 3.Ver inventario \n 4.Comprar  \n 5.Eliminar prodcuto del carrito \n 6.Pagar \n 7.Salir")



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
            eliminar_prod()    
        elif opcion == 6:
            pagar()
                
        elif opcion == 7:    
            break     
        else:
            print("No esta esa opcion")   
    except:
        print("Por favor, ingresa un numero correcto! ")        

