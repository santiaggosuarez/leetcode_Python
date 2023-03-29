# Código para crear carpetas nuevas en Google Drive.

import os
from google.colab import drive
drive.mount("/content/drive")

# Contador de carpetas creadas hasta el momento
count = 10

for i in range(10):
  path = "/content/drive/MyDrive/BIOMETRIC-SS/Dataset de pinturas - SS/Fakes - SS/"

  count += 1
  # Las carpetas se guardarán enumeradas con 4 dígitos, las siguientes líneas se utilizarán para mantener el formato (nn0001, nn0002, nn0045, nn0999, nn4599, etc)
  if count < 10:
    zeros = "nn000"
  elif count < 100:
    zeros = "nn00"
  elif count < 1000:
    zeros = "nn0"
  else:
    zeros = "nn"

  # Creamos el nombre de la carpeta
  new_folder_name = zeros + str(count)
  # Creamos la carpeta
  new_folder_path = os.path.join(path, new_folder_name)
  # Evitamos que se genere una excepción si la carpeta ya existe.
  os.makedirs(new_folder_path, exist_ok=True)

  print(f"Carpeta {new_folder_name} creada con éxito.")
