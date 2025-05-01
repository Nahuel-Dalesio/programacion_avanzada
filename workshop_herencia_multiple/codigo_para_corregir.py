
# Explicar por qué imprime lo que imprime y cómo se puede modificar el orden de herencia.

class A:
    def greet(self):
        print("Hi from A")
        
        
        
class B:
    def greet(self):
        print("Hi from B")
        
        
class C(A, B):
    pass
        


obj = C()
obj.greet() #imprime --> Hi from A 

#El orden de herencia lo podemos modificar, cambiando el orden de las clases heredadas por la clase C. 

# obsevación adicional. 
#Para permitir que se ejecute también el método greet() de la clase B, se agrega super().greet() dentro del método greet() de A, lo que hace que Python continúe recorriendo el MRO.

