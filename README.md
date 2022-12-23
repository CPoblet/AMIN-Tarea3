# Tarea 3 - Trabajo de Programación 3
# Algoritmos Metaheurísticos Inspirados en la Naturaleza
## Propósito del Trabajo

Desarrollar una aplicación que implemente el Problema de la Mochila a través del método de Extremal Optimisation utilizando el lenguaje de programación Python junto a las bibliotecas Numpy, Pandas, Sys y Time.

Primero se debe de definir como modelar la mochila para contener los elementos a colocar en su interior tal que maximice la función objetivo. El código debe de tener al menos las siguientes funciones:

-Generar un número real randóminco entre [0 y 1].
-Generar un número entero randomico entre [1 y N].
-Inicializar el ecosistema.
-Función de evaluación del fitness de cada especie.
-Función de selección de una especie usando el método de la ruleta.
-Función de reemplazo de la especie seleccionada.
-Función de evaluación del ecosistema.
Además se deben ingresar y/o sintonizar los siguientes parámetros:
-Archivo de entrada.
-Valor semilla generador valores randómicos.
-Condición de término o número de iteraciones.
-Valor de Tau (τ ).

## Manual de Usuario 🛠️
Ingresar a https://github.com/CPoblet/AMIN-Tarea3/, presionar el botón verde que dice "Code" y seleccionar posteriormente "Download ZIP".
Una vez descargado el archivo AMIN-Tarea3-main.zip (Es necesario descargar WinRAR para descomprimir), se debe apretar click derecho y "Extraer aquí".
Una vez descomprimido, se requerirá la aplicación visual studio code (descargable desde este link: https://code.visualstudio.com/).
Una vez descargado e instalado el programa, se deberá ir a la pestaña "extensiones", buscar la siguiente extension e instalarla:

- Python

Una vez instaladas se deberá ir a la pestaña archivo y abrir la carpeta descomprimida con anterioridad, una vez abierta la carpeta se deberá localizar el archivo llamado main.py y abrirlo, en la zona superior existirá pestaña llamada "Terminal", pulsarla y seleccionar "Nuevo Terminal", una vez abierta la terminal escribir el siguiente sin comillas:

~~~ 
 pip install numpy
~~~

Esto instalará el numpy el cual es necesario para la ejecución del programa, una vez finalizado escribir en la terminal el siguiente sin comillas:

- "python main.py semilla tamaño_tablero tamaño_población probabilidad_cruza probabilidad_mutación número_iteraciones"
~~~ 
 python main.py 1 8 40 90 5 40
~~~

Los argumentos (semilla tamaño_tablero tamaño_población probabilidad_cruza probabilidad_mutación número_iteraciones) deben ser numero enteros positivos.
## Este programa fue realizado en 🛠️
* [Visual Studio Code](https://code.visualstudio.com) - Visual Studio Code es un editor de código fuente desarrollado por Microsoft para Windows, Linux, macOS y Web.
* [Python 3.10.0](https://www.python.org/downloads/release/python-3100/) - Lenguaje de programación.
## Autores ✒️
* **Marcelo Calderón** - *Código - Documentación* - [Marchel0](https://github.com/Marchel0)
* **Nicolás Cereceda** - *Código - Documentación* - [Nishiorman](https://github.com/Nishiorman)
* **Carlos Poblete** - *Código - Documentación* - [CPoblet](https://github.com/CPoblet)
