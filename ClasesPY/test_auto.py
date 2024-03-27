from auto import Auto

# imprimir_auto=Auto("Kia","santos",2020)
# print(imprimir_auto.__dict__)
# imprimir_auto.actualizar_kilometraje(1000)
# print(f"\nEl nuevo kilometraje es: {imprimir_auto.kilometraje} km")
# imprimir_auto.realizar_viaje(100000)
# print(f"\nRealizando viaje a: {imprimir_auto.kilometraje} km")
# print(f"\nEl estado del auto es: {imprimir_auto.estado_auto()}")

auto_actual_toyota = Auto.auto_toyota()
otro_auto = Auto.crear_auto(marca="Toyota",modelo="Safari", anio=2023,kilometraje=0)

print("Auto actual Toyota:", auto_actual_toyota)
print("Otro auto:", otro_auto)
print("Mismo kilometraje:", Auto.comparar_kilometraje(auto_actual_toyota, otro_auto))
print("Diferencia de años entre los autos:", Auto.comparar_anio(auto_actual_toyota, otro_auto))


