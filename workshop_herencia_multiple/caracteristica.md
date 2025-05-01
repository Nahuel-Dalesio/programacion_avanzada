# Herencia multiple
## Pregunta teórica:

**¿Qué es la herencia múltiple y qué problema puede generar en lenguajes como Python?**

La herencia múltiple es un concepto en programación orientada a objetos donde una clase puede heredar atributos y métodos de más de una clase base.

En Python, la herencia múltiple, puede plantear problemas debido a posibles ambigüedades o conflictos que surjan cuando una clase hereda métodos o atributos de dos o más clases que tienen métodos o atributos con el mismo nombre.

El problema principal es conocido como el "problema del diamante" o "diamante de la muerte", que ocurre cuando una subclase hereda de dos superclases que a su vez heredan de una misma superclase común. Esto puede resultar en ambigüedades sobre cuál método o atributo debe prevalecer en la subclase, ya que Python sigue un orden de resolución de métodos específico llamado MRO (Method Resolution Order).

[¡Codigo del "problema diamante"!](ej_prob_diamante.py)

## ✅Mini autoevaluación
1. ¿Qué es el orden de resolución de métodos (MRO)?

    El orden de resolución de métodos (MRO) en Python es la regla que determina el orden en que se buscan los métodos y atributos cuando se llama a super() o se accede a un método en una jerarquía de clases, especialmente en herencia múltiple.

2. ¿Qué conflicto puede surgir si dos clases tienen el mismo método y una clase hereda
de ambas?

    El problema principal es conocido como el "problema del diamante" o "diamante de la muerte", que ocurre cuando una subclase hereda de dos superclases que a su vez heredan de una misma superclase común. Esto puede resultar en ambigüedades sobre cuál método o atributo debe prevalecer en la subclase, ya que Python sigue un orden de resolución de métodos específico llamado MRO (Method Resolution Order).

## **Código con errores para corregir**

- [¡Resolución!](codigo_para_corregir.py)

## **Ejercicio práctico:**

- [¡Resolución!](ejercicio_practico.py)

## Reflexión individual

¿En qué casos usarías herencia múltiple y en cuáles preferirías composición?

### Herencia múltiple

Es recomendable usarla cuando una clase realmente necesita comportamientos combinados de múltiples clases base, y esas clases representan tipos funcionales independientes.

**Casos recomendables :**

- Cuando querés reutilizar código de varias clases pequeñas y bien definidas.

- Cuando las clases base no comparten estado complejo.

- Cuando usás mixins, es decir, clases diseñadas solo para añadir comportamiento auxiliar.

### Composición

Cuando querés combinar comportamientos complejos o dependencias dinámicas sin acoplar fuertemente las clases entre sí.

**Casos recomendables :**

- Cuando una clase **"tiene un"** componente, no **"es un"** tipo de ese componente.

    ej:
    
    - Si tu frase dice "es un tipo de", probablemente te conviene usar herencia.

    - Si tu frase dice "tiene un", usá composición.

- Para mayor flexibilidad y reutilización sin heredar jerarquías.

- Cuando querés modularidad y sustituir componentes fácilmente.


