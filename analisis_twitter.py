
import json
import pandas as pd
import re
import matplotlib.pyplot as plt

print("PROYECTO: ANALISIS DE SENTIMIENTOS DE X")
print("----------------------------------------")

# Leer el archivo JSON
with open("publicaciones.json", "r", encoding="utf-8") as documento:
    datos = json.load(documento)

publicaciones = datos["publicaciones"]

# Palabras clave para identificar sentimientos
palabras_positivas = [
    "feliz", "excelente", "increíble", "encanta",
    "motivado", "emocionado", "interesante", "éxito"
]

palabras_negativas = [
    "decepcionado", "mal", "perdí", "preocupado",
    "problemas", "triste", "difícil", "frustrado"
]

# Clasificar el sentimiento de cada publicación

def analizar_sentimiento(texto):
    texto = texto.lower()

    expresiones_negativas = [
        "no me gustó",
        "esperaba algo mejor"
    ]

    if any(expresion in texto for expresion in expresiones_negativas):
        return "Negativo"

    # Identificar palabras completas, evitando coincidencias parciales
    palabras_texto = set(
        re.findall(r"\b[\wáéíóúüñ]+\b", texto)
    )

    positivas = len(palabras_texto.intersection(palabras_positivas))
    negativas = len(palabras_texto.intersection(palabras_negativas))

    if positivas > negativas:
        return "Positivo"
    elif negativas > positivas:
        return "Negativo"
    else:
        return "Neutral"


    # Detectar expresiones negativas completas
    expresiones_negativas = [
        "no me gustó",
        "esperaba algo mejor"
    ]

    if any(expresion in texto for expresion in expresiones_negativas):
        return "Negativo"

    positivas = sum(
        palabra in texto for palabra in palabras_positivas
    )

    negativas = sum(
        palabra in texto for palabra in palabras_negativas
    )

    if positivas > negativas:
        return "Positivo"
    elif negativas > positivas:
        return "Negativo"
    else:
        return "Neutral"


# Crear una tabla con Pandas
df = pd.DataFrame(publicaciones)

# Aplicar el análisis a los textos
df["sentimiento"] = df["texto"].apply(analizar_sentimiento)

# Mostrar los resultados
print("\nRESULTADOS DEL ANALISIS DE SENTIMIENTOS")
print("----------------------------------------")
print(df[["id", "usuario", "texto", "sentimiento"]].to_string(index=False))

# Contar publicaciones por sentimiento
resumen = df["sentimiento"].value_counts()

print("\nRESUMEN DE SENTIMIENTOS")
print("----------------------------------------")
print(resumen)

# Crear una figura con dos graficas
fig, ejes = plt.subplots(1, 2, figsize=(12, 5))

# Grafica de barras
resumen.plot(
    kind="bar",
    ax=ejes[0],
    title="Cantidad de publicaciones por sentimiento"
)

ejes[0].set_xlabel("Sentimiento")
ejes[0].set_ylabel("Cantidad de publicaciones")
ejes[0].tick_params(axis="x", rotation=0)

# Grafica circular
resumen.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ejes[1],
    title="Distribucion porcentual de sentimientos"
)

ejes[1].set_ylabel("")

# Ajustar espacios y mostrar graficas
plt.tight_layout()
plt.savefig("grafica_sentimientos.png", dpi=300)
plt.show()

print("\nGrafica guardada como grafica_sentimientos.png")

# Exportar resultados a un archivo CSV
df.to_csv(
    "resultados_sentimientos.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Resultados guardados en resultados_sentimientos.csv")
