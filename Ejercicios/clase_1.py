# Ejercicio 2:
# Definir una función denominada IMPRIMIR_MENSAJE que imprima el siguiente mensaje en pantalla "Estudiando en la UNAB". No recibe ninguna información, por lo tanto no tiene ningún parámetro formal.

# def imprimir_mensaje():
#     print("Estudiando en la UNAB") 
# imprimir_mensaje()

# Ejercicio 3:
# Definir una fumción denominada RETORNO_MENSAJE que retorne el siguiente mensaje: "Estudiando en la Unab"
# A. ¿Cómo hago para mpstrar ese mensaje en pantalla?
# B. ¿Qué diferencia encuentra con el ejercicio anterior?
# C. Si tuviera que imprimir mensaje como "Estudiando Matemática I en la UNAB" y "Estudiando Python en la UNAB" utilizando la misma función ¿Cómo la modificarías?

# # A.
# def retorno_mensaje():
#     return "Estudiando en la UNAB" 
# print(retorno_mensaje())

# # C.
# a = "Estudiando Matemática I en la UNAB"
# b = "Estudiando Python en la UNAB" 
# def mensaje(a,b):
#     print(f"{a} y {b}")
# mensaje(a,b)
# Ejercicio 4:
# Definir una función denominada IMPRIMO_FECHA que reciba tres cadenas de caracteres como parámetros formales, que representan un día, un mes y un año e imprima la fecha de la siguiente manera: "21 de septiembre de 2025"

# def imprimir_fecha(dia,mes,ano):
#     print (f"{dia} de {mes} de {ano}")
# imprimir_fecha(25,"septiembre",2025)

# Ejercicio 5:
# Definir una función denominada CUANTOS_DIAS que reciba el numero de mes como parámetro y retorne la cantidad de días que posee. Ejemplo: CUANTOS_DIAS(1). Debería retornar 31.
# Ayuda:Pensar en tener una lista de la siguiente manera: [["Enero",31],["Febrero", 28],...]
# meses = ["Enero 31","Febrero 28","Marzo 31","Abril 30","Mayo 31","Junio 30","Julio 31","Agosto 31","Septiembre 30","Octubre 31","Noviembre 30","Diciembre 31"]

# def cuantos_dias(mes):
#     for m in meses:  
#         if 1 <= mes <= 12:
#             return(meses[mes-1])
#         else:
#             return "el número ingresado no es correcto"
        
# dia = cuantos_dias(12)
# print(dia)

# Ejercicio 6:
# Definir una función que reciba un número como parametro y mostrar la tabla de multiplicar de dicho número. 

# def imprimir_tabla(num):
#     for f in range(1,11):
#         multiplos = num * f
#         print (multiplos)
# imprimir_tabla(9)

# Ejercicio 7:
# Definir una función que calcule el área de un círculo, otra que calcule el área de un rectángulo y otra que calcule el área de un cuadrado. Analice que parámetros debería recibir dichas funciones.
# import math 
# def area_circulo(r):
# 	a = r**2*math.pi
# 	print (a)

# def area_rectangulo (b,a):
#     a = b*a
#     print(a)

# def area_cuadrado(l):
#     a=l**2
#     print(a)

# area_circulo(2)
# area_rectangulo(2)
# area_cuadrado(2)

# ---------------------------------------------------------------------------------------------

# Ejercicio 8:
# Definir una función llamada CALCULO_REBAJA que reciba dos números, uno con el precio anterior y otro para el precio rebajado y devuelva un número que represente el porcentaje rebajado.

# def calculo_rebaja(num,num1):
#     p=num-num1
#     por=(100*p)/num
#     print(f"{por}%")
# calculo_rebaja(20,2)

# Ejercicio 9:
# Definir una función llamada CALCULO_NUEVO_PRECIO que reciba dos números, uno con el precio anterior y otro con el número de porcentaje a aumentar y devuelva el precio aumentado. 
# def calculo_nuevo_precio(num,num1):
#     a=num*num1/100
#     precio=int(a+num)
#     print(f"${precio}")
# calculo_nuevo_precio(100,50)

# Ejercio 10:
# definir una función llamada CALCULO_TRANSPORTE que reciba cuatro números: la cantidad de alumnos de 1era, 2da y 3er. Salita de un jardin de infantes y la cantidad de asientos del transporte escolar. La función debe retornar cuántos micros necesito contratar para una excursión sabiendo que cada salita es acompañada por tres adultos.
# import math
# def calculo_transporte(p,s,t,tr):
#     a = 3
#     asientos = p+s+t+a*3
#     micros = math.ceil(asientos/tr)
#     return micros
# m=calculo_transporte(20,20,20,70)
# print(m)

# Ejercicio 11:
# Definir una función llamada ARMO_CARTEL que reciba una cadena de caracteres (para el nombre del producto) y dos números (el precio anterior y el otro para el precio rebajado) e imprima un cartel de la siguiente forma:
# Atención!!! Gran rebaja para el producto nombre (rebido como parametro)
# Antes: Precio anterior
# Ahora: Precio rebajado
# def armo_cartel(prod,pv,pn):
#     print(f"Atención!!! Gran rebaja para el producto {prod}\nAntes: ${pv}\nAhora: ${pn}")
# armo_cartel("remera", 12000,10000)

# Ejercico 12:
# Definir una función llamada CALCULO_LITROS  que reciba tres números, el alto, ancho y profundidad (en metros) de una pileta y devuelva la cantidad de litros que tiene.

# def calculo_litros(al,an,prof):
#     litros=al*an*prof 
#     # pileta rectangular
#     return litros

# Ejercicio 13:
# Definir una función llamada A_PAGAR que reciba 4 números: la cantida de personas, el monto gastado en bebida, el monto gastado en comida y el alquiler del lugar, y retorne cuánto le toca pagar a cada uno.
# def a_pagar(p,beb,com,alq):
#     monto=int((beb+com+alq)/p)
#     print (f"Tiene que pagar cada uno: ${monto}")
# a_pagar(4,10000,10000,20000)

# Ejercicio 14:
# Definir tres funcines llamadas CONVERTIR_A_DOLAR, CONVERTIR_A_EURO Y CONVERTIR_A_REAL. Cada función recibe un parámetro que representa un monto en pesos y devuelve su conversión respectiva. 

# def convertir_a_dolar(m):
#     conv= m * 1068.55
#     print(conv)
# def convertir_a_euro(m):
#     conv= m * 1154.36
#     print(conv)
# def convertir_a_real(m):
#     conv= m * 185.74
#     print(conv)
        
# Ejercico 15:
# Definir una función llamada CALCULO_DOSIS que reciba tres números. Uno para la cantidad de días que debe suministrar el remedio, el segundo dato para la cantidad de veces por día que debe tomarlo, y el último dato para la cantidad de comprimidos que trae el envase. La función debe devolver verdadero si el envase alcanza para ese tratamiento y falso si no alcanza.

# def calculo_dosis (sum,vec,comp):
#     t=comp-sum*vec
#     if t < 0:
#         return False
#     else:
#         return True
# p = calculo_dosis(1,3,4)
# print(p)

# Ejercicio 16:
# Definir una función llamada PRECIO_CON_IVA que agrega el IVA (21%) de un producto dado su precio de venta sin IVA.
# def precio_con_iva(precio):
#     pci= precio*1.21
#     print(pci)
# precio_con_iva(100)