
import tweepy
from tkinter import Tk, simpledialog

print("PROYECTO: CONEXION CON LA API DE X")
print("----------------------------------")

# Solicitar el Bearer Token de forma privada
ventana = Tk()
ventana.withdraw()

bearer_token = simpledialog.askstring(
    "Autenticacion X",
    "Introduce tu Bearer Token:",
    show="*"
)

ventana.destroy()

if not bearer_token:
    print("No se introdujo ningun token.")
    raise SystemExit

# Crear el cliente de Tweepy
cliente = tweepy.Client(
    bearer_token=bearer_token
)

print("\nCliente de Tweepy configurado correctamente.")
print("No se realizo ninguna consulta a X.")
print("No se solicitaron publicaciones ni se generaron cargos.")
