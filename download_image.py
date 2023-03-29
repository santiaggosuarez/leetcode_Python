import requests, os
from bs4 import *

def download_image(url, path, name):
    """
    Función para descargar una imagen. Recibe el link de dicha imagen, una ruta y el nombre que queremos ponerle

    Args:
      url: string que contiene la URL de la imagen a descargar
      path: string que contiene la ruta en la que se guardará la imagen
      name: string que contiene el nombre y extensión de la imagen
    """

    full_path = path + name
    response = requests.get(url)
    with open(full_path, "wb") as img:
        img.write(response.content)

    print(f"{name} se ha descargado con éxito.")
