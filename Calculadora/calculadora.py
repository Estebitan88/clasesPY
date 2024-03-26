print("CALCULADORA")
print("***********")

valor_alto=float(input("Ingresar el valor del alto: "))
valor_ancho=float(input("Ingresar el valor del ancho: "))

area_rectangulo=(valor_alto*valor_ancho)
perimetro_rectangulo = 2 * (valor_alto + valor_ancho)
superficie_rectangulo=(valor_alto*valor_ancho)

print("RESULTADO")
print("***********")

print(f"Area del rectangulo: {area_rectangulo}")
print(f"Perimetro del rectangulo: {perimetro_rectangulo}")
print(f"Superficie del rectangulo: {superficie_rectangulo}","metros cuadrados")