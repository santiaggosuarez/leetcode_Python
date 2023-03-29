# Código utilizado para renombrar archivos con su extensión correspondiente.

import imghdr, os
from google.colab import drive
drive.mount("/content/drive")
count = 109

folder = "/content/drive/MyDrive/Carpeta para pruebas/"
content = os.listdir(folder)

for image in content:
  # Obtenemos el formato de la imagen
  format_image = imghdr.what(folder + image)
  # Si no tiene formato nos saltamos la iteración
  if format_image is None:
    continue

  count += 1
  # Las imágenes se guardarán enumeradas con 4 dígitos, las siguientes líneas se utilizarán para mantener el formato (nn0001, nn0002, nn0045, nn0999, nn4599, etc)
  if count < 10:
    zeros = "nn000"
  elif count < 100:
    zeros = "nn00"
  elif count < 1000:
    zeros = "nn0"
  else:
    zeros = "nn"

  # Creamos el nuevo nombre de la imagen
  new_name_image = zeros + str(count) + "." + format_image

  # Renombramos la imagen
  original_path = os.path.join(folder, image)
  new_path = os.path.join(folder, new_name_image)
  os.rename(original_path, new_path)
    
  print(f"{image} >>> {new_name_image}")
