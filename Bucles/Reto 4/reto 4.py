datosIngresados = input("Ingrese datos:")

datos = []

for i in datosIngresados:
    if i.isdigit():
        datos.append(float(i)) 
    elif i.isalpha:
        datos.append(i)
    else:
        print("El dato ingresado no es válido.")

print(f"Su lista de datos: {datos}")






