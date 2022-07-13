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
    
    def registro (self):
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

if __name__ == '__main__':
    test=persona('Sebastian','Paul','Rosero','Macías','Los Rios','Babahoyo','123471234',47)
    print(test.nombre)
    print(test.nombre2)
    print(test.apellido)
    print(test.apellido2)
    print(test.ciudad)
    print(test.provincia)
    print(test.cedula)
    print(test.edad)
    print("=======================")
    print("Personas Discapacidad")
    personasD=personaDiscapacidad('Ronald','Aarón','Zambrano','Malave','Ambato','Tungurahua','123471234', 45)
    print(personasD.nombre)
    print(personasD.nombre2)
    print(personasD.apellido)
    print(personasD.apellido2)
    print(personasD.ciudad)
    print(personasD.provincia)
    print(personasD.cedula)
    print(personasD.edad)
    print("=======================")
    print("Personas Discapacidad")
    personasB=personaBajosRecursos('Alexis','Diego','Espin','Ramirez','Puyo','Pastaza ','125361612', 65)
    print(personasB.nombre)
    print(personasB.nombre2)
    print(personasB.apellido)
    print(personasB.apellido2)
    print(personasB.ciudad)
    print(personasB.provincia)
    print(personasB.cedula)
    print(personasB.edad)
