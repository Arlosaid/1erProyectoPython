almacen = ["Cafe","Leche","Huevos","Cereal","Tortillas","Jabon"]
precio = [15,20,5,28,10,18]  
      
            
print("""
--------------------------------------
      Bienvenidos a mi tienda
--------------------------------------      
""")
print("Menu \n\n 1.Ver almacen \n 2.Agregar prodcuto al almacen \n 3.Eliminar producto del almacen \n 4.Salir")

menu_principal = int(input("Ingrece su opcion ->"))

while menu_principal != 0 :
   
    if menu_principal == 1:
        for inventario, costo in zip(almacen,precio):
            print("\n",inventario," - ",costo) 

    elif menu_principal == 2:
        producto = input("Agregue producto: ").capitalize()
        if producto in almacen:
                print("\nEste producto ya esta en el almacen")
        else:
            costo = int(input("Agregue el precio: "))
            almacen.append(producto) 
            precio.append(costo)
    
    elif menu_principal == 3:
            
            eliminar = input("Que producto desea eliminar: ").capitalize()
            if eliminar not in almacen:
                print("\nEste producto no se encuentra en el almacen")
            else:
                for i in range(len(almacen)-1,-1,-1):
                    if almacen[i] == eliminar:
                     almacen.pop(i)
                     precio.pop(i)
                     print("\nSe elimino el producto\n")   
    
    
        

    elif menu_principal == 4:
        print("Gracias por usar este sistema")
        break        
   
    else:
        print("Elija una opcion valida en el menu")    
    
    print("""
    --------------------------------------
      Bienvenidos a mi tienda
    --------------------------------------      
    """)
    print("Menu \n\n 1.Ver almacen \n 2.Agregar producto al almacen \n 3.Eliminar producto del almacen \n 4.Salir")

    menu_principal = int(input("Ingrece su opcion ->"))      
    