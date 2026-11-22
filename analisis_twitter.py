
import json
import pandas as pd
import re
import matplotlib.pyplot as plt

print("PROYECTO: ANALISIS DE SENTIMIENTOS DE X")
print("----------------------------------------")

# 1. Leer los datos del archivo JSON
try:
    with open("publicaciones.json", "r", encoding="utf-8") as documento:
        datos = json.load(documento)

    publicaciones = datos["publicaciones"]

except FileNotFoundError:
    print("Error: No se encontro el archivo publicaciones.json")
    raise SystemExit

except (json.JSONDecodeError, KeyError):
    print("Error: El archivo JSON no tiene el formato esperado.")
    raise SystemExit

# 2. Definir palabras clave
palabras_positivas = [
    "feliz", "excelente", "increible", "encanta",
    "motivado", "emocionado", "interesante", "exito"
]

palabras_negativas = [
    "decepcionado", "mal", "perdi", "preocupado",
    "problemas", "triste", "dificil", "frustrado"
]

# 3. Funcion para clasificar sentimientos
def analizar_sentimiento(texto):

    texto = str(texto).lower()

    expresiones_negativas = [
        "no me gusto",
        "esperaba algo mejor"
    ]

    if any(expresion in texto for expresion in expresiones_negativas):
        return "Negativo"

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


# 4. Crear DataFrame con Pandas
df = pd.json_normalize(publicaciones)

# Verificar que existan las columnas necesarias
columnas_necesarias = ["id", "usuario", "texto"]

if not all(columna in df.columns for columna in columnas_necesarias):
    print("Error: Faltan columnas necesarias en el archivo JSON.")
    raise SystemExit

if df.empty:
    print("No hay publicaciones para analizar.")
    raise SystemExit

# 5. Aplicar el analisis de sentimientos
df["sentimiento"] = df["texto"].apply(analizar_sentimiento)

# 6. Mostrar publicaciones clasificadas
print("\nRESULTADOS DEL ANALISIS")
print("----------------------------------------")

print(
    df[["id", "usuario", "texto", "sentimiento"]]
    .to_string(index=False)
)

# 7. Calcular cantidades y porcentajes
categorias = ["Positivo", "Negativo", "Neutral"]

resumen = df["sentimiento"].value_counts().reindex(
    categorias, fill_value=0
)

porcentajes = (resumen / len(df)) * 100

print("\nRESUMEN DE SENTIMIENTOS")
print("----------------------------------------")

for categoria in categorias:
    print(
        f"{categoria}: {resumen[categoria]} "
        f"publicaciones ({porcentajes[categoria]:.1f}%)"
    )

print(f"\nTotal de publicaciones analizadas: {len(df)}")

# 8. Crear graficas
fig, ejes = plt.subplots(1, 2, figsize=(12, 5))

resumen.plot(
    kind="bar",
    ax=ejes[0],
    title="Cantidad de publicaciones por sentimiento"
)

ejes[0].set_xlabel("Sentimiento")
ejes[0].set_ylabel("Cantidad de publicaciones")
ejes[0].tick_params(axis="x", rotation=0)

resumen.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ejes[1],
    title="Distribucion porcentual de sentimientos"
)

ejes[1].set_ylabel("")

plt.tight_layout()

# 9. Guardar grafica
plt.savefig("grafica_sentimientos.png", dpi=300)

# 10. Exportar resultados a CSV
df.to_csv(
    "resultados_sentimientos.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nARCHIVOS GENERADOS")
print("----------------------------------------")
print("Grafica: grafica_sentimientos.png")
print("Resultados: resultados_sentimientos.csv")

plt.show()

print("\nAnalisis finalizado correctamente.")
