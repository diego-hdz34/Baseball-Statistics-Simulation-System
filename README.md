# **Baseball Statistics & Simulation System**

Este proyecto es una aplicación de terminal de nivel profesional desarrollada en Python, diseñada para el procesamiento automatizado, análisis estadístico avanzado y simulación predictiva de partidos de la liga de béisbol. El sistema implementa una arquitectura basada en la ingesta de datos desde archivos planos, el cálculo preciso de métricas de Sabermetría (colectivas e individuales) y un motor de emparejamiento predictivo basado en el rendimiento histórico.  
Desarrollado como una solución de software clave dentro de la Escuela de Ingeniería Informática de la Universidad Católica Andrés Bello (UCAB).

## **1\. Características Principales**

* **Ingesta Dinámica y Tolerancia a Fallos:** Implementación de un sistema de lectura de archivos con redundancia de rutas dinámicas (*fallback paths*) para garantizar la disponibilidad de los datos de origen bajo diferentes entornos de despliegue.  
* **Procesamiento de Métricas de Sabermetría:** Computación en tiempo real de estadísticas complejas utilizando algoritmos que previenen activamente errores de desbordamiento y división por cero:  
  * *Métricas de Pitcheo:* Efectividad (EFE), WHIP (Walks plus Hits per Innings Pitched) y Ratio de Ponches por Base por Bola (P/BB).  
  * *Métricas de Bateo:* Promedio de Bateo (PRO), Porcentaje de Embasado (OBP) y Slugging (SLG).  
  * *Métricas de Defensa:* Porcentaje de Fildeo (F%), Total de Lances (TL) y Doble Plays por Juego (DP/J).  
* **Motor de Simulación Competitiva:** Algoritmo de emparejamiento predictivo que evalúa el rendimiento ofensivo, defensivo y de pitcheo acumulado entre dos franquicias (seleccionadas por el usuario o de manera aleatoria) para determinar un ganador estadístico a través de un sistema de puntuación ponderada.  
* **Persistencia de Reportes:** Automatización de la persistencia de datos mediante la exportación de tablas de posiciones, lideratos y simulaciones directamente a un archivo plano histórico (*Tablas\_estadisticas.txt*).  
* **Interfaz de Usuario Centrada (CLI):** Consola interactiva estructurada estéticamente con rutinas dinámicas de limpieza de pantalla según el sistema operativo y renderizado tabular de alta fidelidad visual mediante *PrettyTable*.

## **2\. Arquitectura de Software y Flujo de Datos**

El sistema se rige bajo un flujo de datos desacoplado en tres capas fundamentales:  
\[Capa de Datos: Archivos .txt\] ──\> \[Capa de Negocio: Algoritmos e Ingesta\] ──\> \[Capa de Presentación: CLI / PrettyTable\]

### **Parser y Tokenizador**

La función centralizada de procesamiento mapea el archivo plano buscando tokens y delimitadores de control estructurados (como @@@@@, \*\*\*\*\*, &&&&&, \!\!\!\!\!). Este algoritmo actúa como un parser que segmenta y distribuye las filas crudas en colecciones indexadas de diccionarios nativos, simulando el comportamiento de un mapeador objeto-relacional (ORM) ligero.

### **Modelado de Datos (Estructuras Nativas)**

Se diseñaron modelos estructurados para representar fielmente las entidades del dominio deportivo:

* **Equipo:** Identificador, Juegos Jugados (JJ), Juegos Ganados (JG), Juegos Perdidos (JP), Average (AVE) y Diferencia de Juegos (DIF).  
* **Pitcher / Bateador / Defensor:** Perfiles individuales asociados de forma lógica a sus respectivos equipos mediante claves foráneas basadas en el identificador único del equipo.

## **3\. Tecnologías Utilizadas**

| Tecnología / Componente | Propósito en el Proyecto   |
| :---- | :---- |
| **Python 3.x** | Lenguaje de programación principal para el desarrollo de la lógica de negocio. |
| **PrettyTable** | Librería de terceros encargada del formateo y estructuración de matrices de datos en la interfaz de consola. |
| **os / sys** | Interactividad con las llamadas del sistema para operaciones de E/S y control de pantalla del sistema operativo. |
| **random** | Generación de variables pseudoaleatorias para el módulo de simulación automatizada. |

## **4\. Instalación y Despliegue**

1. Descargue o clone el repositorio en su estación de trabajo local.  
2. Asegúrese de instalar las dependencias necesarias ejecutando en su terminal:  
   pip install prettytable  
3. Posicione el archivo de datos origen denominado archivo\_proyecto\_final.txt en el mismo directorio raíz que el archivo del script ejecutable.  
4. Inicie la aplicación mediante el intérprete de Python:  
   python proyecto.py

## **5\. Competencias de Ingeniería Demostradas**

* **Lógica Algorítmica Avanzada:** Uso intensivo de expresiones lambda integradas para realizar operaciones eficientes de ordenamiento descendente y búsqueda de valores máximos en estructuras complejas de datos.  
* **Desarrollo Defensivo:** Manejo explícito de excepciones I/O para prevenir caídas accidentales del sistema ante la ausencia de archivos externos.  
* **Clean Code y Modularización:** Alta cohesión y bajo acoplamiento mediante la división estricta de responsabilidades (funciones exclusivas para cálculos matemáticos puros versus funciones de interfaz de usuario).
