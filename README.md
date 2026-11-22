# Actividad 6. Análisis de sentimientos de X mediante Python

## 1. Descripción del proyecto

El proyecto consiste en desarrollar una aplicación en Python orientada al análisis de sentimientos de publicaciones relacionadas con X (anteriormente Twitter).

Se utilizan herramientas de procesamiento de datos y visualización para clasificar publicaciones en tres categorías: positivas, negativas y neutrales.

## 2. Objetivo

Aplicar herramientas de Python para procesar información estructurada en formato JSON, analizar textos y representar los resultados mediante gráficas, considerando la integración de la API de X mediante Tweepy.

## 3. Tecnologías utilizadas

- Python 3.9
- Tweepy 4.17
- Pandas
- Matplotlib
- JSON
- Visual Studio Code

## 4. Archivos del proyecto

| Archivo | Función |
|---|---|
| `analisis_twitter.py` | Procesamiento y análisis de sentimientos. |
| `conexion_x.py` | Configuración del cliente de Tweepy mediante Bearer Token. |
| `publicaciones.json` | Datos de ejemplo utilizados para el análisis. |
| `resultados_sentimientos.csv` | Resultados exportados. |
| `grafica_sentimientos.png` | Representación gráfica de los resultados. |

## 5. Metodología

1. Preparación de los datos en formato JSON.
2. Lectura y procesamiento de información con Pandas.
3. Identificación de palabras clave positivas y negativas.
4. Clasificación de publicaciones en tres categorías.
5. Cálculo de cantidades y porcentajes.
6. Elaboración de gráficas con Matplotlib.
7. Exportación de resultados a CSV.
8. Configuración del cliente de Tweepy para la integración con la API de X.

## 6. Resultados obtenidos

Se analizaron 10 publicaciones de ejemplo:

| Sentimiento | Cantidad | Porcentaje |
|---|---:|---:|
| Positivo | 5 | 50 % |
| Negativo | 4 | 40 % |
| Neutral | 1 | 10 % |

## 7. Integración con la API de X

Se desarrolló un archivo adicional denominado `conexion_x.py`, que utiliza la biblioteca Tweepy para configurar un cliente mediante Bearer Token.

La configuración se ejecutó correctamente de manera local. Sin embargo, no se realizaron solicitudes de extracción de publicaciones, debido a que la cuenta de desarrollador no disponía de créditos para utilizar los servicios de lectura de la API.

## 8. Limitaciones

Los datos utilizados para el análisis son ficticios y se emplearon con fines demostrativos. No representan publicaciones reales descargadas de X.

La clasificación de sentimientos utiliza un método basado en palabras clave, por lo que no constituye un modelo avanzado de procesamiento de lenguaje natural.

La conexión con Tweepy fue configurada, pero no se verificó la autenticación ante los servidores de X ni se realizó extracción de datos.

## 9. Conclusión

El desarrollo permitió aplicar conocimientos de programación en Python, manejo de archivos JSON, procesamiento de datos con Pandas y visualización con Matplotlib.

Asimismo, se exploró la integración de una API mediante Tweepy, identificando los requisitos de autenticación y las limitaciones de acceso relacionadas con los créditos disponibles.

El proyecto constituye una base funcional para desarrollar posteriormente un sistema de análisis de publicaciones reales y apoyar la interpretación de información para la toma de decisiones.

## 10. Autora

Proyecto académico correspondiente a la Actividad 6 de la asignatura Uso de Big Data.

**Lenguaje de programación:** Python.
