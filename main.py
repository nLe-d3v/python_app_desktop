from tkinter import *
from tkinter import ttk
from conexion import *

#Creamos una clase para hacer el registro , con sus metodos
class Registro(Frame):
    #Principal
    def __init__(self,master,*args,**kwargs):
        #Constructor
        super().__init__(master,*args,**kwargs)

        #Frames (divs)
        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2,column=0,row=0)
        self.frame2= Frame(master)
        self.frame2.grid(column=0,row=1)
        self.frame3= Frame(master)
        self.frame3.grid(rowspan=2,column=1,row=1)

        self.frame4 = Frame(master , bg='navy')
        self.frame4.grid(column=2,row=1) 

        #Variables string
        self.nombre = StringVar()
        self.color = StringVar()
        self.tipo = StringVar()

        self.buscar = StringVar(self)

        #Invocamos a la clase de MYSQL
        self.base_datos = Registro_datos()
        self.create_widgets()

    #Crear las ventanas del programa
    def create_widgets(self):
        #Labels , entrys with var , buttons
        Label(self.frame1,text='REGISTRO \t DE \t DATOS', bg='green', fg='black').grid(column=0,row=0)

        Label(self.frame2,text="Nombre").grid(column=0 , row=1)
        caja_nombre = Entry(self.frame2,textvariable=self.nombre)
        caja_nombre.grid(column=1,row=1)

        Label(self.frame2,text="Color").grid(column=0,row=2)
        caja_color = Entry(self.frame2,textvariable=self.color)
        caja_color.grid(column=1,row=2)
        
        Label(self.frame2,text="Tipo").grid(column=0,row=3)
        caja_tipo = Entry(self.frame2,textvariable=self.tipo)
        caja_tipo.grid(column=1,row=3)

        bt_añadir = Button(self.frame2,text="Añadir producto").grid(column=0,row=5)
       
        bt_modificar = Button(self.frame2,text="Modificar producto").grid(column=1,row=5)

        bt_eliminar= Button(self.frame2,text="Eliminar producto").grid(column=0,row=6)

        bt_buscar= Button(self.frame2,text="Buscar productos").grid(column=1,row=6)

        bt_mostrar = Button(self.frame2,text="Mostrar registro").grid(column=0,row=7)

        #Creamos una tabla 
        self.tabla = ttk.Treeview(self.frame3,height=21)
        self.tabla.grid(column=0,row=0)

        #Sus respectivos scroll
        ladoX = Scrollbar(self.frame3,orient=HORIZONTAL,command=self.tabla.xview)
        ladoX.grid(column=0,row=1,sticky="EW")
        ladoY = Scrollbar(self.frame3,orient=VERTICAL,command=self.tabla.yview)
        ladoY.grid(column=1,row=0,sticky="ns")

        #Configuramos sus scrolls
        self.tabla.configure(xscrollcommand= ladoX.set , yscrollcommand= ladoY.set)
        self.tabla["columns"] = ("Nombre" , "Color" , "Tipo")

        #Columnas de cada tabla
        self.tabla.column("#0",minwidth=100,width=120,anchor="center")
        self.tabla.column("Nombre" , minwidth=100 , width=130 , anchor="center")
        self.tabla.column("Color" , minwidth=100 , width=120 , anchor="center")
        self.tabla.column("Tipo" , minwidth=100 , width=120 , anchor="center")

        #Encabezados de cada columna (campos)
        self.tabla.heading("#0" , text="Id" , anchor="center")
        self.tabla.heading("Nombre" , text="Nombre" , anchor="center")
        self.tabla.heading("Color" , text="Color" , anchor="center")
        self.tabla.heading("Tipo" , text="Tipo" , anchor="center")

        #Estilo para la tabla
        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt')
        estilo.configure("Treeview" , foreground = "white")
        estilo.map("Treeview" , background =[("selected" , "green2")],foreground = [("selected" , "black")])

        # self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        
    def agregar_datos(self):
        self.tabla.get_children()
        nombre = self.nombre.get()
        color = self.color.get()
        tipo = self.tipo.get()

        datos = (nombre,color,tipo)
        if(nombre and color and tipo != ""):
            self.tabla.insert("" , 0,text= nombre , values=datos)
            self.base_datos.insertarData(nombre,color,tipo)

    def mostrar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrarData()
        i = 1
        for dato in registro:
            self.tabla.insert("",i,text=registro[1][1:2] , values = registro[i][2:6])

    # def eliminar_datos(self):
    #     fila = self.tabla.selection()
    #     if len(fila) != 0 :
    #         nombre = ("'" , str(self.nombre))

def main():
    ventana = Tk()
    ventana.title("App prueba")
    app = Registro(ventana)
    app.mainloop()

if __name__ == "__main__":
    main()

