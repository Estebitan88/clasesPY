from laptop import Laptop
from laptop_gaming import Laptop_Gaming

def imprimir_informe(laptop):
    informe = laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"{clave}: {valor}")
    print("\n")

laptop_pepito = Laptop("Lenovo", "i7", 32, 600)
laptop_juanito = Laptop_Gaming("MSI", "i7", 16, "RTX 8GB")

print("PEPITO:")
imprimir_informe(laptop_pepito)
print("JUANITO:")
imprimir_informe(laptop_juanito)
