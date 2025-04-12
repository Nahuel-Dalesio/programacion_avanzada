# Ejercicio 1:
# ● Conforme equipos de trabajo de 2 (a lo sumo 3) estudiantes
# ● Crear un carpeta en su equipo de trabajo de nombre unab_pa_tp_3. 
# ● Asociar su IDE de preferencia con la carpeta creada anteriormente
# ● Cree un archivo README.md con los objetivos del presente taller
# ● Publique su proyecto en GitHub (debe hacer desde la cuenta de uno de los integrantes del equipo,
# invitar a los otros integrantes y al docente a la cuenta felipemoralesquerol)

# ------------------------------------------------------------------------ #

# Ejercicio 2:
# ● Crear la clase Punto con dos atributos x e y (ambos numéricos), con el correspondiente
# constructor que recibe ambos valores.
# ● Definir métodos tales como:
# ○ eje_x
# ○ eje_y
# ○ impresion (método que devuelve en representación de string ambos valores)
# ○ opuesto (método que devuelve el punto opuesto -es decir con los atributos
# negativos-)
# ○ Cualquier otro método que considere importante

class Punto():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def get_eje_x(self):
        return self.x
    
    def get_eje_y(self):
        return self.y
    
    def set_eje_x(self,nx):
        self.x = nx
        
    def set_eje_y(self,ny):
        self.y = ny
    
    def impresion(self):
        return f"el punto se encuentra en ({self.x},{self.y})"
    
    def opuesto(self):
        return Punto(-self.x,-self.y)
    
    def __str__(self):
        return self.impresion()

# instancia de clase Punto():
# p = Punto(2,3)
# x= p.set_eje_x(4)
# y= p.set_eje_y(6)
# o=p.opuesto()
# print(p)
# print(o)

# ------------------------------------------------------------------------ #

# Ejercicio 3:
# Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que
# pasa la línea en un espacio de dos dimensiones.
# La clase dispondrá de los siguientes métodos:
# ● Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase
# Punto, que son utilizados para inicializar los atributos.
# ● mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
# ● mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
# ● mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
# ● mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique.

class Linea():
    def __init__(self,punto_a,punto_b):
        self.a = punto_a
        self.b = punto_b
        
    def desplazar_derecha(self,dist):
        # TODO deberia haber un condional que solo permita numeros mayores a 1
        self.a.set_eje_x(self.a.get_eje_x()+dist)
        self.b.set_eje_x(self.b.get_eje_x()+dist)
        return f"La linea se desplazo a la derecha {dist} unidades, ahora inicia en el punto: ({self.a.get_eje_x()},{self.a.get_eje_y()}) ; ({self.b.get_eje_x()},{self.b.get_eje_y()})"
    
    def desplazar_izquierda(self,dist):
        # TODO deberia haber un condional que solo permita numeros menores a 0 
        self.a.set_eje_x(self.a.get_eje_x()+dist)
        self.b.set_eje_x(self.b.get_eje_x()+dist)
        return f"La linea se desplazo a la izquierda {dist} unidades, ahora inicia en el punto: ({self.a.get_eje_x()},{self.a.get_eje_y()}) ; ({self.b.get_eje_x()},{self.b.get_eje_y()})"
    
    def desplazar_arriba(self,dist):
        self.a.set_eje_y(self.a.get_eje_y()+dist)
        self.b.set_eje_y(self.b.get_eje_y()+dist)
        return f"La linea se desplazo hacia arriba {dist} unidades, ahora inicia en el punto: ({self.a.get_eje_x()},{self.a.get_eje_y()}) ; ({self.b.get_eje_x()},{self.b.get_eje_y()})"
    
    def desplazar_abajo(self,dist):
        self.a.set_eje_y(self.a.get_eje_y()+dist)
        self.b.set_eje_y(self.b.get_eje_y()+dist)

# instancia de clase Linea():   
p1 = Punto(2,3)
p2 = Punto(4,6)

l=Linea(p1,p2)

ld = l.desplazar_derecha(2)
print(ld)
li = l.desplazar_izquierda(-2)
print(li)
la = l.desplazar_arriba(2)
print(la)

# ------------------------------------------------------------------------ #

# Ejercicio 4:
# Desarrolla una clase Cancion con los siguientes atributos:
# ● titulo: una variable String que guarda el título de la canción.
# ● autor: una variable String que guarda el autor de la canción.
# Con los siguientes métodos:
# ● Cancion(String, String): constructor que recibe como parámetros el título y el autor de la
# canción (por este orden).
# ● get_titulo(): devuelve el título de la canción.
# ● get_autor(): devuelve el autor de la canción.
# ● set_titulo(String): establece el título de la canción.
# ● set_autor(String): establece el autor de la canción


class Cancion():
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    
    def set_titulo(self,tn):
        self.titulo = tn
    def set_autor(self,an):
        self.autor = an
        
# Ejercicio 5:
# ● Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre
# cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar
# (ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes
# servicios: getters y setters, método para leer la información y método para mostrar la
# información.
# ● Este último método mostrará la información del libro con este formato:
# Título: Introduction to Java Programming 3a. edición
# Autor: Liang, Y. Daniel
# ISBN: 0-13-031997-X
# Prentice-Hall, New Jersey (USA)
# viernes 16 de noviembre de 2001
# 784 páginas
       
class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido

    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_apellido(self, apellido):
        self.apellido = apellido

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, ciudad, pais, fecha_edicion):
        self.titulo = titulo
        self.autor = autor 
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.ciudad = ciudad
        self.pais = pais
        self.fecha_edicion = fecha_edicion

    def get_titulo(self):
        return self.titulo
    def get_isbn(self):
        return self.isbn
    def get_autor(self):
        return self.autor
    def get_paginas(self):
        return self.paginas
    def get_edicion(self):
        return self.edicion
    def get_editorial(self):
        return self.editorial
    def get_ciudad(self):
        return self.ciudad
    def get_pais(self):
        return self.pais
    def get_fecha_edicion(self):
        return self.fecha_edicion
       
    def set_titulo(self, titulo):
        self.titulo = titulo
    def set_autor(self, autor):
        self.autor = autor
    def set_isbn(self, isbn):
        self.isbn = isbn
    def set_paginas(self, paginas):
        self.paginas = paginas
    def set_edicion(self, edicion):
        self.edicion = edicion
    def set_editorial(self, editorial):
        self.editorial = editorial
    def set_ciudad(self, ciudad):
        self.ciudad = ciudad
    def set_pais(self, pais):
        self.pais = pais
    def set_fecha_edicion(self, fecha_edicion):
        self.fecha_edicion = fecha_edicion

    def mostrar_informacion(self):
        return f"Título: {self.titulo} {self.edicion}\n Autor: {self.autor}\n(ISBN: {self.isbn}\n{self.editorial}, {self.ciudad} {self.pais}\n{self.fecha_edicion}\npagina: {self.paginas}"
    def __str__(self):
        return self.mostrar_informacion()

per = Persona("Nahuel","Dalesio")
libro = Libro("Cien años de soledad",per,"978-84-376-0494-7",471,"1a. edición","Editorial Sudamericana","Buenos Aires","Argentina","martes 30 de mayo de 1967")
print(libro.mostrar_informacion())
