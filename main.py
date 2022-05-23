from tkinter import *
from guizero import *
import tkinter as aux

# Definición de la aplicación y la propiedad de ancho y alto
app = App(layout="grid")
app.height = 720
app.width = 1280
app.bg="lavender"


# Definición de funciones para funcionamiento de la aplicación

comidas=[["Caldo de costilla", 8000],
 ["Caldo de birria",12000],
  ["Pescado frito", 18000],
   ["Chicarrón con arepa", 10000],
    ["Sancocho trifásico", 15000],
     ["Chunchullo con arepa", 8000],
      ["Pollo frito", 12000],
       ["Arepa con todo", 10000],
        ["Bandeja con res o cerdo", 12000],
         ["Aborrajado", 5000],
          ["Empanada", 1000],
           ["Chorizo", 4000],
            ["Chuzo", 4000],
             ["Calentado", 11000],
              ["Chuleta", 18000],
               ["Huevos al gusto", 6000]
               ]

bebidas = [["Gatorade", 4000],
 ["Cerveza", 6000],
  ["Chocolate", 3000],
   ["Café", 3000],
    ["Soda Bretaña", 2000],
     ["Te helado", 6000],
      ["Vive 100", 2500],
       ["Speed Max", 2000],
        ["Milo frío o caliente", 4000],
         ["Pedialyte", 8000],
          ["Jugos electrolíticos", 6500],
           ["Leche", 3000],
            ["Jugo de naranja", 4000],
             ["Gaseosa", 2500],
              ["Jugo de mandarina", 5000],
               ["Agua", 2000]]

varios = [["Dolex", 1000],
 ["Acetaminofen", 800],
  ["Bonfiest", 2500],
   ["Alka Zetser", 1000],
    ["Ibuprofeno", 800],
     ["Advil Max", 2000]]

preciosComida=[8000,12000,18000,10000,15000,8000,12000,10000,12000,5000,1000,4000,4000,11000,18000,6000]
preciosBebida=[4000,6000,3000,3000,2000,6000,2500,2000,4000,8000,6500,3000,4000,2500,5000,2000]
preciosVarios=[1000,800,2500,1000,800,2000]
iva = 0.19
def factura():
    facturaT = ""
    acumComida = 0
    acumBebida = 0
    acumVarios = 0
    totalNeto = 0
    facturaText.enabled = True
    
    for x in range(16):
        widgetCantidad = foodBox.tk.grid_slaves(x+1, 2)
        widgetNombre = foodBox.tk.grid_slaves(x+1,0)
        cantidad = int(widgetCantidad[0].get())
        acumComida += 1
        if cantidad > 0:
            facturaT += widgetNombre[0].cget("text") + ": \n"
            precio = cantidad*comidas[acumComida-1][1]
            facturaT += "Cantidad:" + str(cantidad)  +". Precio Total: " + str(precio) +"\n"
            totalNeto += precio 
    
    for x in range(16):
        widgetCantidad = drinksBox.tk.grid_slaves(x+1, 2)
        widgetNombre = drinksBox.tk.grid_slaves(x+1, 0)
        cantidad = int(widgetCantidad[0].get())
        acumBebida += 1
        if cantidad > 0:
            facturaT += widgetNombre[0].cget("text") + ": \n"
            precio = cantidad*bebidas[acumBebida-1][1]
            facturaT += "Cantidad: " + str(cantidad) + ". Precio: " + str(precio) +"\n"
            totalNeto += precio

    for x in range(6):
        widgetCantidad = othersBox.tk.grid_slaves(x+1, 2)
        widgetNombre = othersBox.tk.grid_slaves(x+1, 0)
        cantidad = int(widgetCantidad[0].get())
        acumVarios += 1
        if cantidad > 0:
            facturaT += widgetNombre[0].cget("text") + ": \n"
            precio = cantidad*varios[acumVarios-1][1]
            facturaT += "Cantidad: " + str(cantidad) +". Precio: " + str(precio) +"\n"
            totalNeto += precio
    facturaT += "Precio Neto: " + str(totalNeto) + "\n IVA: " + (str(totalNeto*iva)) + "\n Precio Total:" + (str(totalNeto + (totalNeto*iva)))
    facturaText.tk.delete(1.0, END)
    facturaText.tk.insert(aux.INSERT, facturaT)
    facturaText.tk.configure(state = "disabled")

def cambiarIva():
    def modificar():
        global iva
        iva = float(ivaTextBox.tk.get())
        ventana.hide()
    ventana = Window(app,title="Cambiar valor de IVA", layout="grid", height=80)
    ventana.hide()
    ivaTextBox = TextBox(ventana,height=15,width=50,grid=[0,0])
    cambiarBoton = PushButton(ventana,command= modificar,text="Aceptar", grid=[1,0], width=20)
    ventana.show(wait=True)

def limpiar():
    for x in range(16):
        widgetCantidad = foodBox.tk.grid_slaves(x+1, 2)
        widgetCantidad[0].delete(0, END)
        widgetCantidad[0].insert(0,"0")
    
    for x in range(16):
        widgetCantidad = drinksBox.tk.grid_slaves(x+1, 2)
        widgetCantidad[0].delete(0, END)
        widgetCantidad[0].insert(0,"0")

    for x in range(6):
        widgetCantidad = othersBox.tk.grid_slaves(x+1, 2)
        widgetCantidad[0].delete(0, END)
        widgetCantidad[0].insert(0,"0")
    
    factura()

# Caja de título de la aplicación
titleBox = Box(app, width=1280, height=120 ,grid=[0,0,4,1], border= True)
titleBox.tk.configure(background="purple1")
nombreRestaurante = Text(titleBox,"Desenguayabe Food", size=32, color = "white", align="top", bg="purple1")
lema = Text(titleBox,"Gordo y sin plata, pero no borracho", size= 24, color="white", align="top", bg="purple1")

foodBox = Box(app, layout="grid",  width=320, height=480, grid=[0,1], border=True)
foodBox.tk.configure(background="lightblue")
tituloAlimentos = Text(foodBox,"Comidas", grid=[0,0], align="top", bg="lightblue")
iterador = 1
for x in comidas:
    nombre = Text(foodBox, x[0], grid=[0,iterador], align="left", bg="lightblue")
    precio = Text(foodBox, x[1], grid=[1,iterador],align="left", bg="lightblue")
    cantidad = TextBox(foodBox,"0",grid=[2,iterador])
    iterador += 1
for x in range(3):
    relleno = Text(foodBox,"             ", grid=[0,x+17], align="left", bg="lightblue")


drinksBox = Box(app, layout="grid", width=320, height=480, grid=[1,1], border=True)
drinksBox.tk.configure(background="lightblue")
tituloBebidas = Text(drinksBox,"Bebidas", grid=[0,0], align="top", bg="lightblue")
iterador = 1
for x in bebidas:
    nombre = Text(drinksBox,x[0],grid=[0,iterador], align="left", bg="lightblue")
    precio = Text(drinksBox, x[1], grid=[1,iterador],align="left", bg="lightblue")
    cantidad = TextBox(drinksBox,"0",grid=[2,iterador])
    iterador += 1
for x in range(3):
    relleno = Text(drinksBox,"             ", grid=[0,x+17], align="left", bg="lightblue")


othersBox = Box(app, layout="grid", width=400, height=480,  grid=[2,1],border=True)
othersBox.tk.configure(background="lightblue")
tituloVarios = Text(othersBox,"Varios", grid=[0,0], align="top", bg="lightblue")
iterador = 1
for x in varios:
    nombre = Text(othersBox,x[0],grid=[0,iterador], align="left", bg="lightblue")
    precio = Text(othersBox, x[1], grid=[1,iterador],align="left", bg="lightblue")
    cantidad = TextBox(othersBox,"0",grid=[2,iterador])
    iterador += 1
for x in range(13):
    relleno = Text(othersBox,"             ", grid=[0,x+7], align="left", bg="lightblue")




orderBox = Box(app,width=320,height=480, grid=[3,1],border=True)
orderBox.tk.configure(background="lightblue")
tituloFactura = Text(orderBox,"Factura", align="top", bg="lightblue")
facturaText = TextBox(orderBox, text="", scrollbar=True,enabled=False, height="fill", width="fill", multiline=True)
facturaText.bg ="lightblue"

buttonBox = Box(app, height=120,width=1280,grid=[0,2,4,1],border=True)
buttonBox.tk.configure(background="mediumpurple")

botonFactura =  PushButton(buttonBox,command=factura, text="Generar Factura", align="right")
botonLimpiar = PushButton(buttonBox,command=limpiar, text="Limpiar Valores", align="right")
botonModificar = PushButton(buttonBox,command=cambiarIva, text="Modificar IVA", align="right")

app.display()