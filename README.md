# 1. PROTECTORA DE ANIMÁLES

Nuestro trabajo se centra en el funcionamiento de una base de datos para una protectora de animales. Para realizarla, hemos empleado distintas técnicas aprendidas a lo largo del curso de programación orientada a objetos (POO).

## 2. Arquitectura del Código

A continuación, una explicación de los conceptos técnicos empleados:

* **Herencia:** Las clases `Perro` y `Gato` heredan de la clase base `Animal`.
* **Herencia Múltiple:** Contamos con una clase `Voluntario`, que es un usuario que realiza trabajos en el refugio, comportándose tanto como usuario como trabajador.
* **Clase Abstracta:** La clase `Empleado`, por ejemplo, usa la abstracción para indicar que todo empleado debe implementar el método para indicar su trabajo.
* **Clases Públicas y Privadas (Encapsulamiento):** La clase `Empleado` cuenta con atributos privados, definiendo el `DNI` como algo privado.

## 3. Características Principales

El programa permite realizar las siguientes acciones:

* Registrar nuevos ingresos de animales.
* Gestión de los estados de adopción.
* Asignación de cuidadores y dietas específicas.

## 4. Requisitos e Instalación

* **Lenguaje:** Python
* **Comando para ejecutarlo:**
    ```bash
    python main.py
    ```
