from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business

laptop_pepito=Laptop("lenovo","i7",32,600)
laptop_maria=Laptop("lenovo","i7",32,600)

laptop_juanito=Laptop_Gaming("MSI","I7",4,"RTX 8GB")



laptop_negocios = Laptop_Business("asus", "I7", 4, "Instalados antivirus","Disponibilidad de Wi-Fi")
print(laptop_negocios.realizar_diagnostico_sistema())



#print(laptop_juanito.realizar_diagnostico_sistema())
#asus_laptop=Laptop.asus_laptop()

# print(laptop_pepito.__dict__)
# print(laptop_pepito.valor_final())
# print(f"el valor de descuento: {laptop_pepito.valor_descuento(10)}")

# for numero in range(1,1001):
#     asus_laptop=Laptop.asus_laptop(numero)
#     print(asus_laptop.__dict__)

# print (Laptop.comparar_costo(laptop_pepito,laptop_maria))