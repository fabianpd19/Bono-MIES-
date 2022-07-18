import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from uuid import getnode
import pymongo

class persona:
    '''
    Clase para poder determinar cada uno de los datos detalladamente de cada uno
    de los usuarios, para tener un control sobre cada uno los mismos y poder determinar sus 
    necesidades
    ---
    Atributos
    --------
    nombre: str
        Primer nombre del usuario
    nombre2: str
        Segundo nombre del usuario
    apellido: str
        Primer apellido del usuario
    apellido2: str
        Segundo apellido del usuario
    ciudad: str
        Ciudad de donde proviene el usuario
    provincia: str
        Provincia de la ciudad de donde proviene el usuario
    cedula: str
        Cedula de identidad del usuario
    edad: int
        Edad del usuario
    Métodos
    -------
    __init__(self, nombre, nombre2, apellido, apellido2, ciudad, provincia, cedula, edad):
        Constructor de cada uno de los atributos de nuestra clase persona
    
    registro(self):
        Recolección de los datos en una base de datos para determinar el bono a recibir

    '''
    def __init__(self, nombre, nombre2, apellido, apellido2, ciudad, provincia, cedula, edad):
        self.nombre=nombre
        self.nombre2=nombre2
        self.apellido=apellido
        self.apellido2=apellido2
        self.ciudad=ciudad
        self.provincia=provincia
        self.cedula=cedula
        self.edad=edad
    
    def registro (self, user, password):
        self.user=user
        self.password=password
        pass

class personaDiscapacidad (persona):
    '''
    Subclase de la clase persona. 
    Clase para determinar las necesidades en específico de una persona con discapcidad
    y así calcular el bono a recibir
    ---
    Atributos (Todos los atributos son heredados de la clase principal persona)
    --------
    Métodos
    -------
    __init__(self, nombre, nombre2, apellido, apellido2, ciudad, provincia, cedula, edad):
        Constructor de cada uno de los atributos
    carnetDiscapcidad (self):
        Método para la respectiva verificación del carnet de discapacidad

    '''
    def __init__(self, nombre, nombre2, apellido, apellido2, ciudad, provincia, cedula, edad):
        super().__init__(nombre, nombre2, apellido, apellido2, ciudad, provincia, cedula, edad)
    def carnetDiscapcidad (self):
        pass

class personaBajosRecursos (persona):
    '''
    Subclase de la clase persona. 
    Clase para determinar las necesidades en específico de una persona con discapcidad
    y así calcular el bono a recibir
    ---
    Atributos (Todos los atributos son heredados de la clase principal persona)
    --------
    Métodos
    --------
    '''
    def __init__(self, nombre, nombre2, apellido, apellido2, ciudad, provincia, cedula, edad):
        super().__init__(nombre, nombre2, apellido, apellido2, ciudad, provincia, cedula, edad)

def mostrarTabla():
    '''Función para acceder a todos los datos que se encuentre dentro de la basee de datos'''
    pass

def all_Information_admin ():
    '''Mostrar información interna de la base de datos (solo personal autorizado)'''
    ventana=tkinter.Tk()
    ventana.geometry("1200x720")
    tabla=ttk.Treeview(ventana, columns=4)
    tabla.grid(row=4, column=0, columnspan=4)
    tabla.heading("#0", text="ID")
    tabla.heading("#1", text="nombre")
    ventana.mainloop()

def agregarInfoMongoVentana():
    '''Recopilar información de los usuarios que se vayan a registrar por primera vez'''
    '''Crear ventana de la interfaz'''
    ventana = tkinter.Tk()
    '''Asignación de medidas'''
    ventana.geometry("500x500")
    '''Texto'''
    ingresoTkM=tkinter.Label(ventana, text="--Ingrese sus datos--\n")
    ingresoTkM.pack()
    '''Texto'''
    mostrarTkMessage=tkinter.Label(ventana, text="Nombre:")
    mostrarTkMessage.pack()
    '''Entrada de texto del primer nombre'''
    nombreTk = tkinter.Entry(ventana)
    nombreTk.pack()
    '''Texto'''
    mostrarTkMessage=tkinter.Label(ventana, text="Segundo nombre:")
    mostrarTkMessage.pack()
    '''Entrada de texto del segundo nombre'''
    nombre2Tk = tkinter.Entry(ventana)
    nombre2Tk.pack()
    mostrarTkMessage=tkinter.Label(ventana, text="Apellido:")
    mostrarTkMessage.pack()
    '''Entrada de texto del primer apellido'''
    apellidoTk = tkinter.Entry(ventana)
    apellidoTk.pack()
    mostrarTkMessage=tkinter.Label(ventana, text="Segundo apellido:")
    mostrarTkMessage.pack()
    '''Entrada de texto del segundo apellido'''
    apellido2Tk = tkinter.Entry(ventana)
    apellido2Tk.pack()
    mostrarTkMessage=tkinter.Label(ventana, text="Ciudad:")
    mostrarTkMessage.pack()
    '''Entrada de texto de la ciudad del usuario'''
    ciudadTk = tkinter.Entry(ventana)
    ciudadTk.pack()
    mostrarTkMessage=tkinter.Label(ventana, text="Provincia:")
    mostrarTkMessage.pack()
    '''Entrada de texto de la provincia (ciudad) del usuario'''
    provinciaTk = tkinter.Entry(ventana)
    provinciaTk.pack()
    mostrarTkMessage=tkinter.Label(ventana, text="Cedula:")
    mostrarTkMessage.pack()
    '''Entrada de texto de la cédula de identidad del usuario'''
    cedulaTk = tkinter.Entry(ventana)
    cedulaTk.pack()
    mostrarTkMessage=tkinter.Label(ventana, text="Edad:")
    mostrarTkMessage.pack()
    '''Entrada de texto de la edad del usuario'''
    edadTk = tkinter.Entry(ventana)
    edadTk.pack()
    mostrarTkMessage=tkinter.Label(ventana, text="Género:")
    mostrarTkMessage.pack()
    '''Entrada de texto del genero del usuario'''
    generoTk = tkinter.Entry(ventana)
    generoTk.pack()
    mostrarTkMessage=tkinter.Label(ventana, text="\n")
    mostrarTkMessage.pack()

    '''Función para obtener lasa cadenas de los datos ingresados en la interfaz'''
    def getDatos ():
        getNombre=nombreTk.get()
        getNombre2=nombre2Tk.get()
        getApellido=apellidoTk.get()
        getApellido2=apellido2Tk.get()
        getCiudad=ciudadTk.get()
        getProvincia=provinciaTk.get()
        getCedula=cedulaTk.get()
        getEdad=edadTk.get()
        getGenero=generoTk.get()
        # print(getNombre)
        # print(getNombre2)
        # print(getApellido)
        # print(getApellido2)
        # print(getCiudad)
        # print(getProvincia)
        # print(getCedula)
        # print(getEdad)
        # print(getGenero)
        '''Creación de un diccionario con los datos ingresados'''
        datosDic={'nombre': getNombre, 'nombre2': getNombre2, 'apellido': getApellido, 'apellido2':getApellido2, 'ciudad': getCiudad, 'provincia': getProvincia, 'cedula': getCedula, 'edad': 30, 'genero':getGenero}
        '''Agregamos nuetro diccionario a nuestra base de datos'''
        updateDic=coleccion.insert_one(datosDic)
    '''Botón que registra los datos ingresados'''
    boton= tkinter.Button(ventana, text="Ingresar datos", command=getDatos)
    boton.pack()
    '''Función para que no se cierre nuestra ventana'''
    ventana.mainloop()

if __name__ == '__main__':

    '''Conectar nuestro programa a MongoDb para la base de datos a utilizar.'''
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    MONGO_BASED = "bono-mies-data"
    COLECCION = "test"
    baseDatos=myClient[MONGO_BASED]
    coleccion = baseDatos [COLECCION]

    '''Ingresar información a MongoDB'''
    agregarInfoMongoVentana()
    
    # ventana = tkinter.Tk()
    # ventana.geometry("500x500")
    # mostrarTexto = tkinter.Entry(ventana)
    # mostrarTexto.pack()
    # boton= tkinter.Button(ventana, text="Inicio sesion", command = textoTerminal)
    # boton.pack()
    # ventana.mainloop()

