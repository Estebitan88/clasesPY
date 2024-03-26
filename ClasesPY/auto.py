class Auto:
    def __init__(self, marca, modelo, anio, kilometraje=0):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.kilometraje=kilometraje

    def mostrarInformacion(self):
        return self.marca+self.modelo+self.anio
    
    
    def actualizar_kilometraje(self, kilometraje):
        if kilometraje < self.kilometraje:
            print("No se puede reducir el kilometraje.")
        else:
            self.kilometraje = kilometraje
    
    def realizar_viaje(self, kilometros):
        if kilometros < 0:
            print("No se aceptan kilómetros en negativo")
        else:
            self.kilometraje += kilometros
    
    def estado_auto(self):
        if self.kilometraje < 20000:
            return "Estoy como nuevo"
        elif 20000 <= self.kilometraje < 100000:
            return "Ya estoy usado"
        else:
            return "Ya déjenme descansar, por favor"

    
imprimir_auto=Auto("Kia","santos",2020)
print(imprimir_auto.__dict__)
imprimir_auto.actualizar_kilometraje(1000)
print(f"\nEl nuevo kilometraje es: {imprimir_auto.kilometraje} km")
imprimir_auto.realizar_viaje(100000)
print(f"\nRealizando viaje a: {imprimir_auto.kilometraje} km")
print(f"\nEl estado del auto es: {imprimir_auto.estado_auto()}")

    
        
    
        
