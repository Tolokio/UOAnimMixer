import tkinter as tk
from tkinter import messagebox
import os

def ejecutar_archivo1():
    os.system("ANIMIXER_TEMPLATE+WEREABLE.py")
    
def ejecutar_archivo2():
    os.system("ANIMIXER_wereable+wereable.py")
    
def ejecutar_archivo3():
    os.system("ANIMREMOVER_wereable-wereable.py")
    
def ejecutar_archivo4():
    os.system("python archivo2.py")
    
def ejecutar_archivo5():
    os.system("python archivo2.py")

def ejecutar_archivo6():
    os.system("ANIMCONVERTER_BMPtoPNG.py")

def ejecutar_archivo7():
    os.system("ANIMCONVERTER_PNGtoBMP.py")

def ejecutar_archivo8():
    os.system("CREATE_FOLDERS.py")


def salir():
    salir = messagebox.askyesno("Quit", "Sure?")
    if salir:
        ventana.destroy()

ventana = tk.Tk()
ventana.title("Interfaz de Menú")

boton1 = tk.Button(ventana, text="TEMPLATE + WEREABLE", command=ejecutar_archivo1)
boton1.pack()
boton2 = tk.Button(ventana, text="WEREABLE + WEREABLE2", command=ejecutar_archivo2)
boton2.pack()
boton3 = tk.Button(ventana, text="WEREABLE - WEREABLE2", command=ejecutar_archivo3)
boton3.pack()
#boton4 = tk.Button(ventana, text="WEREABLE - W2Contorn", command=ejecutar_archivo4)
#boton4.pack()
#boton5 = tk.Button(ventana, text="ONE FOR ALL", command=ejecutar_archivo5)
#boton5.pack()
boton6 = tk.Button(ventana, text="BMP TO PNG", command=ejecutar_archivo6)
boton6.pack()
boton7 = tk.Button(ventana, text="PNG TO BMP", command=ejecutar_archivo7)
boton7.pack()
boton8 = tk.Button(ventana, text="CREATE FOLDERS", command=ejecutar_archivo8)
boton8.pack()
boton9 = tk.Button(ventana, text="QUIT", command=salir)
boton9.pack()

ventana.mainloop()
