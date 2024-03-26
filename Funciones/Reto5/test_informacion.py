import informacion

cantidad_nombres=int(input("Cuantos nombres deseas ingresar: "))
for i in range(cantidad_nombres):
    nombre=input("\nIngrese el nombre: ")
    apellido=input("Ingrese el apellido: ")
    anioNacimiento=int(input("Ingrese el año: "))
    informacion.agregar_nombre(nombre,apellido) 
    informacion.agregar_edad(anioNacimiento)
    
informacion.edad_max()
informacion.edad_min()


