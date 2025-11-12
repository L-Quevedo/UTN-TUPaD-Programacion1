Programación 1
TRABAJO PRACTICO INTEGRADOR - Gestíon de Datos de Países
Integrantes: Juan Aramburu, Lucas Quevedo

Este proyecto es una aplicación de Gestión de Datos de Países desarrollada en Python, cumpliendo con el Trabajo Práctico Integrador de la asignatura Programación 1.

El sistema permite manipular y analizar datos geográficos y demográficos (nombre, población, superfucie y continente) cargados desde un archivo CSV. La aplicación se ejecuta por consola ofreciendo un menú interactivo para que el usuario pueda realiar las siguientes operaciones:
> Adminitración: agregar y actualizar tanto población como superficie de los países
> Consulta: búsqueda por filtro de nombre
> Análisis: filtrado por continente, rango de población o rango de superficie
> Organización: ordenamiento ascendente/descendente por nombre, población o superficie.
> Estadistica: generación de promedios, máximos, mínimos y conteno por continente.



------Intrucciones de uso:-----

Requisitos:
> Tener instalado Python 3.x
> Tener el archivo "dataset.csv en ek mismo directorio que el scritp principal.

Ejecución:
1. Descargue o clone el repositorio completo
2. Abra una terminal o línea de comandos en el directorio del proyecto
3. Ejecute el script principal con el siguiente comando:
> python "TPI - Gestión de datos de países.py"
4. El programa iniciará de forma automatica cargando los datos y mostrando el "menu principal"

Navegación:
Ingrese el número de la opción deseada (ejemplo: 7 para ver la lista completa) y presione 'enter'. Siga las indicaciónes en pantalla para introducir valores de búsqueda, rangos o selecciones de ordenamiento.



-----Ejemplos de entrada y salida:-----

> Ejemplo 1: Mostrar menu principal
Al iniciar el programa:
========================================
      Gestor de Datos de Países
========================================
1. Agregar un país
2. Actualizar Población/Superficie
3. Buscar país por nombre
4. Filtrar países (Continente, Rango, etc.)
5. Ordenar países
6. Mostrar estadísticas
7. Mostrar todos los países
0. Salir
========================================
Ingrese el numero de la opcion correspondiente:_


> Ejemplo 2: Búsqueda por Nombre (opcion 3):
Ingrese el numero de la opcion correspondiente: 3

--- 3. Buscar País por Nombre ---
Ingrese el nombre (o parte del nombre) del país a buscar: argentina

Se encontraron 1 coincidencias para 'argentina':
--------------------------------------------------------------------------------        
  1. Argentina                      | Pob.: 46,000,000      | Sup.: 2,780,000       km² | Cont.: America
--------------------------------------------------------------------------------        
Total de países mostrados: 1


> Ejemplo 3: Mostrar Estadística (opcioón 6)
Ingrese el numero de la opcion correspondiente: 6

--- 6. Estadísticas Globales ---

--- Población ---
País con Mayor Población: India (1,420,000,000)
País con Menor Población: Tonga (106,000)
Promedio de Población Global: 171,128,533.33

--- Superficie ---
Promedio de Superficie Global: 2,263,929.67 km²

--- Continentes ---
Cantidad de países por continente:
  - America: 6 país(es)
  - Europa: 6 país(es)
  - Asia: 6 país(es)
  - Africa: 6 país(es)
  - Oceania: 6 país(es)
----------------------------------------


Participación de los integrantes:

> Alumno/Desarrollador: Quevedo Lucas (comision 8)
> Alumno/Desarrollador: Aramburu Juan (comision 2)