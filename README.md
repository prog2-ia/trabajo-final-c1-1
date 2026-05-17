# 1. PROTECTORA DE ANIMÁLES

Nuestro trabajo se centra en el funcionamiento de una base de datos para una protectora de animales. Para realizarla, hemos empleado distintas técnicas aprendidas a lo largo del curso de programación orientada a objetos (POO).

## 2. Arquitectura del Código

A continuación, una explicación de los conceptos técnicos empleados:

* **Herencia:** Las clases `Perro`, `Gato` y `Caballo` heredan de la clase base `Animal`.
* **Herencia Múltiple:** Contamos con una clase `Voluntario`, que es un usuario que realiza trabajos en el refugio, comportándose tanto como usuario como trabajador.
* **Clase Abstracta:** La clase `Empleado`, por ejemplo, usa la abstracción para indicar que todo empleado debe implementar el método para indicar su trabajo.
* **Clases Públicas y Privadas (Encapsulamiento):** La clase `Empleado` cuenta con atributos privados, definiendo el `DNI` como algo privado.
* **Persistencia de Datos (Archivos Binarios):** Uso de la librería `pickle` para guardar y cargar la base de datos completa de manera automatizada al iniciar y cerrar el sistema.
* **Gestión de Ficheros de Texto:** Escritura automática de informes médicos individuales en formato `.txt` e historial continuo de adopciones.
* **Manejo de Excepciones:** Uso de bloques `try-except` para garantizar una programación defensiva frente a errores de entrada de usuario o de lectura/escritura de archivos.

## 3. Características Principales

El programa permite realizar las siguientes acciones:

* Registrar nuevos ingresos de animales (perros, gatos y caballos).
* Gestión de los estados de adopción con registro histórico automático de fecha y hora.
* Asignación de cuidadores, limpiadores, dietas específicas y control de horas trabajadas.
* Gestión de clientes con opciones para activar membresías de socios o altas de voluntarios.
* Monitorización de múltiples refugios y control de sus capacidades máximas.

## 4. Requisitos e Instalación

* **Lenguaje:** Python
* **Comando para ejecutarlo:**
    ```bash
    python main.py
    ```
