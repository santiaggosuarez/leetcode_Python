import requests
from bs4 import *
import urllib.request

# Función para descargar una imagen. Recibe el link de dicha imagen, una ruta y el nombre que queremos ponerle
def download_image(url, path, name):
  """
  Args:
    url = link de la imagen
    path = ruta dentro del dispositivo
    name = nombre de la imagen, con su extensión
  """
  full_path = path + name
  urllib.request.urlretrieve(url, full_path)
  print(f"{name} se ha descargado con éxito.")

# Site donde están las imágenes que queremos obtener
url = "http://virago347.blogspot.com/2021/"

# User agent obtenido en el navegador para ser utilizado en la obtención de la siguiente variable
user_agent = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}

# Variable para guardar la página web
page = requests.get(url, headers=user_agent)
# Variable para guardar la página web en HTML
page_html = page.content
# Convierto el HTML a un objeto BeautifulSoup para poder trabajarlo
soup = BeautifulSoup(page_html, "html.parser")

# Obtengo los elementos guardados en las etiquetas elegidas
links_images = soup.find_all("a")
page_images = soup.find_all("img")

# Cantidad de imágenes descargadas hasta el momento
count_img = 79

for image in links_images:

  # Para este site obtengo los "href" de las etiquetas "a" porque allí se encuentran las imágenes en mejor resolución
  url_image = image.get("href")
  
  # Verifico que los "href" sean links a imagenes chequeando si finalizan en alguno de los siguientes formatos
  url_image_str = str(url_image).lower()
  if url_image_str[-4:] == ".jpg" or url_image_str[-4:] == ".png" or url_image_str[-5:] == ".webp":

    count_img += 1
    # Las imágenes se guardarán enumeradas con 4 dígitos, las siguientes líneas se utilizarán para mantener el formato (0001, 0002, 0045, 0999, 4599, etc)
    if count_img < 10:
      zeros = "000"
    elif count_img < 100:
      zeros = "00"
    elif count_img < 1000:
      zeros = "0"
    else:
      zeros = ""

    # Nombre con su formato
    image_name = zeros + str(count_img) + ".png"
    # Ruta donde guardar
    image_path = "/content/TEST ORDENADO/"
    download_image(url_image, image_path, image_name)
