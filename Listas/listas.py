
planetas=["Mercurio","Venus","Tierra","Marte","Jupiter","Saturno","Urano","Neptuno"]

# print(planetas[-3])
# print(planetas[2:])
# print(len(planetas))
# print(len(8))

#Trabajar con una lista de numeros 

gravedad_planetas=[0.378,0.907,1,0.377,2.36,0.916,0.889,1.12]
peso_bus=124054

print(f"En la tierra un auto bus de dos pisos pesa {peso_bus} N")
print(f"En mercurio un autobus de dos pisos{peso_bus *gravedad_planetas[0]} N")

print(f"Lo mas liviano que sería un autobus en el sistema solar es: {peso_bus *min(gravedad_planetas)} N")
print(f"Lo mas pesado que sería un autobus en el sistema solar es:{peso_bus *max(gravedad_planetas)} N")

