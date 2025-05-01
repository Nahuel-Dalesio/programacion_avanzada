class A:
    def saludar(self):
        print("Hola desde A")

class B(A):
    def saludar(self):
        print("Hola desde B")

class C(A):
    def saludar(self):
        print("Hola desde C")

# Clase D hereda de B y C → problema del diamante
class D(B, C):
    pass

d = D()
d.saludar()
