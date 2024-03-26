import datetime

datos_paciente=[]
def agregar_nombre (nombre,apellido):
    datos_paciente.append(nombre)
    datos_paciente.append(apellido)

def agregar_edad(anio_nacimiento):
    edad_actual=datetime.datetime.now().year-anio_nacimiento
    datos_paciente.append(edad_actual)

    print("\nDatos de los pacientes:")
    for i in range(0, len(datos_paciente),3):
        nombre = datos_paciente[i]
        apellido = datos_paciente[i+1]
        edad = datos_paciente[i+2]
        print(f"Nombre: {nombre} {apellido}, Edad: {edad}")

def edad_max():
    indice_maximo = datos_paciente.index(max(datos_paciente[2::3]))
    nombre_edad_maxima = datos_paciente[indice_maximo - 2]
    apellido_edad_maxina = datos_paciente[indice_maximo - 1]
    edad_maxima = max(datos_paciente[2::3])
    print(f"\n{nombre_edad_maxima} {apellido_edad_maxina}, con la edad de {edad_maxima} años es mayor a los demás pacientes.")

def edad_min():
    indice_minimo = datos_paciente.index(min(datos_paciente[2::3]))
    nombre_edad_minima = datos_paciente[indice_minimo - 2]
    apellido_edad_minima = datos_paciente[indice_minimo - 1]
    edad_minima = min(datos_paciente[2::3])
    print(f"{nombre_edad_minima} {apellido_edad_minima}, con la edad de {edad_minima} años es menor que los demás pacientes.")


