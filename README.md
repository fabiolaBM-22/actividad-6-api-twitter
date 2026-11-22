# actividad-6-api-twitter
Análisis de sentimientos de publicaciones mediante Python, Pandas y Tweepy
# Actividad 6. Análisis de sentimientos de publicaciones de X con Python

## Descripción del proyecto

Este proyecto consiste en desarrollar una aplicación utilizando Python para realizar un análisis de sentimientos de publicaciones de la red social X (anteriormente Twitter).

El programa permite leer información almacenada en un archivo JSON, procesarla mediante la biblioteca Pandas y clasificar las publicaciones en tres categorías: positivas, negativas y neutrales.

También genera gráficas para representar los resultados y facilita su interpretación.

## Tecnologías utilizadas

- Python 3.9
- Tweepy
- Pandas
- Matplotlib
- JSON
- Visual Studio Code

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `analisis_twitter.py` | Código principal del programa. |
| `publicaciones.json` | Conjunto de publicaciones de ejemplo. |
| `resultados_sentimientos.csv` | Resultados del análisis. |
| `grafica_sentimientos.png` | Gráficas de los sentimientos identificados. |

## Metodología

1. Lectura de publicaciones almacenadas en formato JSON.
2. Procesamiento de los datos con Pandas.
3. Clasificación de sentimientos mediante palabras clave.
4. Conteo de publicaciones positivas, negativas y neutrales.
5. Generación de gráficas con Matplotlib.
6. Exportación de resultados a un archivo CSV.

## Resultados obtenidos

El programa analizó 10 publicaciones de ejemplo y obtuvo los siguientes resultados:

- Positivas: 5
- Negativas: 4
- Neutrales: 1

## Consideraciones

Los datos utilizados en esta versión son publicaciones ficticias creadas para demostrar el funcionamiento del programa. No corresponden a publicaciones extraídas directamente de X mediante su API.

La clasificación se realiza mediante reglas y palabras clave, por lo que constituye un análisis básico de sentimientos.

## Autora

Proyecto académico desarrollado para la Actividad 6 de la asignatura Uso de Big Data.

**Lenguaje:** Python.
