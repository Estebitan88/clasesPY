print("Restaurante Segunda es todo")

print("***Menú*** \n")

listaMenu=["1.Añadir plato al menú.","2.Buscar en el menú.","3.Eliminar plato del menú.","4.Mostrar platos del menú.\n"]
listaPlatos=["Ceviche","Encebollado","Casuela"]

print("\n".join(listaMenu))

opcion=int(input("Elija una opción: "))

if opcion==1:
    print("Platos en el menú:")
    print ("\n".join(listaPlatos))
    anadir=input("Plato a añadir: ")
    listaPlatos.append(anadir)
    print("\n".join(listaPlatos))

if opcion==2:
    print("Buscar Platos en el menú:")
    print ("\n".join(listaPlatos))
    buscar=input("Buscar plato: ")
    if buscar in listaPlatos:
        print(f"{buscar} está en el menú :)")
    else:
        print(f"{buscar} no está en el menú :()")

if opcion==3:
    print("Platos en el menú:")
    print("\n".join(listaPlatos))
    eliminar=input("Plato a eliminar: ")
    
    if eliminar in listaPlatos:
        listaPlatos.remove(eliminar)
        print("\n".join(listaPlatos))
        print(f"Plato eliminado: {eliminar}")
    else:
        print(f"{eliminar} no está en el menú. No se puede eliminar.")

if opcion==4:
    print("Platos en el menú:")
    print("\n".join(listaPlatos))
    

   