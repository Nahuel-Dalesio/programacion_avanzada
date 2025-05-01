
# Define dos clases con métodos distintos (Walker, Runner) y una tercera clase (Athlete) que herede de ambas.
# Crea una instancia y demuestra que puede usar métodos de ambas clases.
# ¿Qué pasa si ambas clases tuvieran un método con el mismo nombre?

class Walker():
    def caminar (self):
        print ("caminando")
class Runner():
    def correr (self):
        print ("corriendo")
class Athlete(Walker,Runner):
    pass

#instancia que demuestra que athlete hereda de ambas clases. 
atleta = Athlete()
atleta.caminar()
atleta.correr()

#Si ambas clases tienen un método con el mismo nombre, se ejecuta el método de la clase que aparece primero en la lista de herencia (según el orden MRO).