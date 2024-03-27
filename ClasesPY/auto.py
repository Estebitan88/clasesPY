import datetime

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
        
    @classmethod
    def auto_toyota(cls):
        fecha_actual = datetime.datetime.now()
        return cls(marca="Toyota", modelo="Safari", anio=fecha_actual.year, kilometraje=0)
    
    @classmethod
    def crear_auto(cls, marca, modelo, anio, kilometraje=0):
        return cls(marca=marca,modelo=modelo, anio=anio, kilometraje=kilometraje)
        
    @staticmethod
    def comparar_kilometraje(auto1,auto2):
        if auto1.kilometraje==auto2.kilometraje:
            return "Los autos tienen el mismo kilometraje"
        return "Los autos no tienen el mismo kilometraje"    

    @staticmethod
    def comparar_anio(auto1, auto2):
        return auto1.anio - auto2.anio
    
    def __str__(self):
        return f"Marca: {self.marca}, Año: {self.anio}, Kilometraje: {self.kilometraje}"


    
        
    
        
