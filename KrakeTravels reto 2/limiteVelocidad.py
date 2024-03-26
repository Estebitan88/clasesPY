import random

print("¡Viaja con KrakeTravels! \n")

print("Por favor escoja un destino:")
print("-Colombia")
print("-Ecuador")
print("-Perú \n")

destino=input("Destino: \n")

velociades=int(input("Velocidad: \n"))
print("URBANA")
print("RURAL")
print("PERIMETRAL")
carreteras=input("Escoja una carretera: \n")

if destino=="Colombia" and velociades>30 and carreteras=="URBANA" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad máxima es 30km/h**\nSu velocidad es: {velociades} km/h \nCuidado está excediendo el límite de velocidad!!!")
elif destino=="Colombia" and velociades<10 and carreteras=="URBANA" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad mínima es 10km/h**\nSu velocidad es: {velociades} km/h \nCuidado está conduciendo muy lento!!!")

elif destino=="Colombia" and velociades>80 and carreteras=="RURAL" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad máxima es 80km/h**\nSu velocidad es: {velociades} km/h \nCuidado está excediendo el límite de velocidad!!!")
elif destino=="Colombia" and velociades<31 and carreteras=="RURAL" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad mínima es 31km/h**\nSu velocidad es: {velociades} km/h \nCuidado está conduciendo muy lento!!!")  

elif destino=="Colombia" and velociades>100 and carreteras=="PERIMETRAL" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad máxima es 100km/h**\nSu velocidad es: {velociades} km/h \nCuidado está excediendo el límite de velocidad!!!")
elif destino=="Colombia" and velociades<81 and carreteras=="PERIMETRAL" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad mínima es 81km/h**\nSu velocidad es: {velociades} km/h \nCuidado está conduciendo muy lento!!!")      
   


elif destino=="Ecuador" and velociades>50 and carreteras=="URBANA" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad máxima es 50km/h**\nSu velocidad es: {velociades} km/h \nCuidado está excediendo el límite de velocidad!!!")
elif destino=="Ecuador" and velociades<10 and carreteras=="URBANA" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad mínima es 10km/h**\nSu velocidad es: {velociades} km/h \nCuidado está conduciendo muy lento!!!")

elif destino=="Ecuador" and velociades>70 and carreteras=="RURAL" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad máxima es 70km/h**\nSu velocidad es: {velociades} km/h\nCuidado está excediendo el límite de velocidad!!!")
elif destino=="Ecuador" and velociades<51 and carreteras=="RURAL" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad mínima es 51km/h**\nSu velocidad es: {velociades} km/h\nCuidado está conduciendo muy lento!!!")

elif destino=="Ecuador" and velociades>90 and carreteras=="PERIMETRAL" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad máxima es 90km/h**\nSu velocidad es: {velociades} km/h\nCuidado está excediendo el límite de velocidad!!!")
elif destino=="Ecuador" and velociades<71 and carreteras=="PERIMETRAL" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad mínima es 71km/h**\nSu velocidad es: {velociades} km/h\nCuidado está conduciendo muy lento!!!")



elif destino=="Perú" and velociades>40 and carreteras=="URBANA" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad máxima es 40km/h**\nSu velocidad es: {velociades} km/h \nCuidado esta excediendo el límite de velocidad!!!")
elif destino=="Ecuador" and velociades<10 and carreteras=="URBANA" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad mínima es 10km/h**\nSu velocidad es: {velociades} km/h \nCuidado esta está conduciendo muy lento!!!")

elif destino=="Perú" and velociades>60 and carreteras=="RURAL" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad máxima es 60km/h**\nSu velocidad es: {velociades} km/h\nCuidado esta excediendo el límite de velocidad!!!")
elif destino=="Perú" and velociades<41 and carreteras=="RURAL" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad mínima es 41km/h**\nSu velocidad es: {velociades} km/h\nCuidado esta está conduciendo muy lento!!!")

elif destino=="Perú" and velociades>120 and carreteras=="PERIMETRAL" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad máxima es 120km/h**\nSu velocidad es: {velociades} km/h\nCuidado esta excediendo el límite de velocidad!!!")
elif destino=="Perú" and velociades<61 and carreteras=="PERIMETRAL" :
    print(f"La carretera en la que esta conduciendo es: {carreteras} \n**La velocidad mínima es 61km/h**\nSu velocidad es: {velociades} km/h\nCuidado esta está conduciendo muy lento!!!")

else:
    print("Escoja bien un destino por favor")