import random

aleatorio= random.randint(1,9)
aleatorio_dos=random.randint(1,9)

if aleatorio==4:
    print("te ganaste un chupete")
elif aleatorio==8:
    print("te ganaste un balón")
elif aleatorio==3 and aleatorio_dos==7:
    print("Te ganaste un televisor")
else:
    print("Perdiste!!!")