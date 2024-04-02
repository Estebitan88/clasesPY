import random

from laptop import Laptop

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria,antivirus,conectividad,costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.antivirus=antivirus
        self.conectividad=conectividad

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico=super().realizar_diagnostico_sistema()
        resultado_oficina =self.realizar_diagnostico_oficina()
        resultado_diagnostico["Resultado oficina"]=resultado_oficina
        return resultado_diagnostico
    
    def realizar_diagnostico_oficina(self):
        resultado_diagnostico= super().realizar_diagnostico_sistema()
        resultado_conectividad=self.verificar_conectividad_red()
        resultado_diagnostico["Resultado conectividad"]=resultado_conectividad
        return resultado_diagnostico
    
    def verificar_conectividad_red(self):
        resultados_conectividad = {}
        resultados_conectividad["Disponibilidad de Wi-Fi"] = random.choice([True, False])
        resultados_conectividad["Acceso a servidores empresariales"] = random.choice([True, False])
        resultados_conectividad["Latencia de red"] = random.randint(1, 100)
        return resultados_conectividad


    pass