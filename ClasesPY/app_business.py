from laptop_business import Laptop_Business
import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.laptops_business = []

        self.root.title("Crear Laptop Business")

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Marca:").grid(row=0, column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)

        ttk.Label(self.root, text="Procesador:").grid(row=1, column=0 )
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1)

        ttk.Label(self.root, text="Memoria:").grid(row=2, column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column=1)

        ttk.Label(self.root, text="Disco:").grid(row=3, column=0)
        self.disco = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.disco).grid(row=3, column=1)

        ttk.Label(self.root, text="Conectividad:").grid(row=4, column=0)
        self.conectividad = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.conectividad).grid(row=4, column=1)

        ttk.Button(self.root, text="Crear Laptop Business", command=self.crear_laptop).grid(row=5, columnspan=2)

        self.mostrar_laptops_business=tk.Text(self.root, height=10,width=50)
        self.mostrar_laptops_business.grid(row=6,column=0,columnspan=2) 

    def crear_laptop(self):
        nueva_laptop_business=Laptop_Business(
            self.marca.get(),self.procesador.get(),self.memoria.get(),
            self.disco.get(),self.conectividad.get())
        self.laptops_business.append(nueva_laptop_business)
    
        print (self.laptops_business[0])

        self.mostrar_laptops_business.insert(tk.END,f"{nueva_laptop_business}")


        self.laptops_business.append(f"{nueva_laptop_business}")
   
        pass

root = tk.Tk()
app = App(root)
root.mainloop()


