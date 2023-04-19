import requests, os, hashlib, json
from bs4 import BeautifulSoup
from PIL import Image
from datetime import datetime

def check_image_size(url, min_size):
    """
    Función para verificar el tamaño de una imagen. Recibe una URL y devuelve True si el tamaño es mayor o igual a "min_size" KB, o False en caso contrario.

    Args:
      url: string que contiene la URL de la imagen a verificar
      min_size: int que contiene el tamaño minimo de la imagen
    """

    response = requests.head(url)

    # Obtenemos el tamaño del archivo de la cabecera HTTP
    if "content-length" in response.headers:
        size = int(response.headers["content-length"])
    else:
        size = None

    # Verificamos si el tamaño es mayor o igual a 40 KB
    if size is not None and size >= min_size * 1024:
        return True
    else:
        return False


def download_image(url, path, name):
    """
    Función para descargar una imagen. Recibe el link de dicha imagen, una ruta y el nombre que queremos ponerle

    Args:
      url: string que contiene la URL de la imagen a descargar
      path: string que contiene la ruta en la que se guardará la imagen
      name: string que contiene el nombre de la imagen
    """

    full_path = path + name
    response = requests.get(url)
    with open(full_path, "wb") as img:
        img.write(response.content)

    print(f"{name} se ha descargado con éxito.")
    
def rename_file(path, old_name, new_name):
    """
    Función para renombrar un archivo. Recibe la ruta del archivo, el nombre actual del archivo y el nuevo nombre que queremos asignarle.

    Args:
      path: string que contiene la ruta del archivo
      old_name: string que contiene el nombre actual del archivo
      new_name: string que contiene el nuevo nombre del archivo
    """

    old_path = os.path.join(path, old_name)
    new_path = os.path.join(path, new_name)
    os.rename(old_path, new_path)

def download_json(data_json, path, name):
    """
    Función para descargar un diccionario en formato JSON. Recibe el diccionario, una ruta y el nombre que queremos ponerle

    Args:
      data_json: diccionario con los datos que queremos guardar en JSON
      path: string que contiene la ruta donde queremos guardarlo
      name: string que contiene el nombre del archivo
    """
    with open(path + name, "w") as f_json:
        # Guardamos y utilizamos ident=2 para que el JSON tenga saltos de linea después de cada coma, y quede mejor a la vista
        json.dump(data_json, f_json, indent=2)

    print(f"{name} se ha descargado con éxito.")

def create_folder(path, name):
    """
    Función para crear una carpeta recibiendo la ruta donde queremos que se cree y el nombre que queremos ponerle
    
    Args:
      path: string que contiene la ruta donde crearemos la carpeta
      name: string que contiene el nombre de la carpeta a crear
    """
    # Creamos la carpeta
    new_folder_path = os.path.join(path, name)
    # Evitamos que se genere una excepción si la carpeta ya existe.
    os.makedirs(new_folder_path, exist_ok=True)
    
    print(f"Carpeta {name} creada con éxito.")



def create_text_file(path, filename, text):
    """
    Función para crear un archivo de texto. Recibe la ruta donde guardar el archivo, el nombre del archivo y el texto a escribir en el archivo

    Args:
        path (str): La ruta donde se desea crear el archivo.
        filename (str): El nombre del archivo que se desea crear.
        text (str): El texto que se desea escribir en el archivo.
    """
    # Abrimos el archivo en modo escritura y especificamos la ruta y el nombre de archivo.
    with open(path + filename, "w") as file:
        # Escribimos el texto especificado en el archivo.
        file.write(text)


def get_extension(image_path, image_name):
    """
    Función para obtener la extensión de una imagen en formato String
    
    Args:
      image_path, image_name: strings que contienen la ruta a la imagen y su nombre actual, juntos forma la ruta completa
    
    Returns:
      retorna un string con el formato de la imagen, ejemplo ".jpg"
    """
    try:
        with Image.open(f"{image_path}/{image_name}") as image:
            image_format = image.format
        if image_format:
            return "." + image_format.lower()
    except (IOError, ValueError):
         return "Error de lectura"


def hash_file(file_path):
    """
    Función para obtener el hash de un archivo utilizando el algoritmo de hashing “SHA256”

    Args:
      file_path: string que contiene la ruta del archivo a hashear

    Returns:
      hash_hex: retorna un string de 64 caracteres con el HASH del archivo
    """

    # Tamaño del bloque para la lectura del archivo (lo utilizamos para mejorar el rendimiento en caso de leer un archivo grande)
    block_size = 65536

    # Creamos un objeto hash SHA256
    hash_sha256 = hashlib.sha256()

    # Abrimos el archivo en modo binario
    with open(file_path, "rb") as file:

        # Leemos el archivo en bloques de tamaño block_size
        block = file.read(block_size)
        
        # Mientras haya bloques que leer, actualizamos el hash con cada bloque
        while len(block) > 0:
            hash_sha256.update(block)
            block = file.read(block_size)

    # Obtenemos el valor hash SHA256 en formato hexadecimal
    hash_hex = hash_sha256.hexdigest()
    return hash_hex



# Variables utiles
query = "prueba"
# Datos para incluir en el JSON
face_type = "fake"
fake_group = "artwork"
fake_type = ""
fake_detailed_type = ""
identified_person = False
url = ""
image_id = ""
operator_id = "SS"
hash = ""
bulk_id = ""
source = "pinterest"

# Contadores para luego nombrar a las variables con id
count_image_id = 1
count_bulk_id = 1

# Le damos formato al bulk_id (4 digitos). Utilizamos zfill para rellenar el string con "0" hasta llegar a 4 digitos
bulk_id = str(count_bulk_id)
bulk_id = bulk_id.zfill(4)

# Lista de URLS obtenido a partir del scraping
list_urls = ["https://i.pinimg.com/564x/9a/9c/a6/9a9ca6d9e41f82319613f6d7ab65c5e4.jpg","https://i.pinimg.com/564x/16/fb/a0/16fba02d5230259f72673ca55543b2f1.jpg","https://i.pinimg.com/564x/a7/7f/21/a77f21e80ce5b70372a3a94908bed446.jpg","https://i.pinimg.com/564x/b6/62/49/b662496b4824f201b00f0253f31d1f8e.jpg","https://i.pinimg.com/564x/c7/44/23/c744232868726bfa97f678a587769f7b.jpg"]

# Iteración donde vamos a descargar las imagenes y crear sus JSON correspondientes
for url_i in list_urls:
    
    # Chequeamos que el tamaño de la imagen sea mayor a 40 KB. Si no es mayor a 40 KB nos saltamos la iteracion
    appropriate_size = check_image_size(url_i, 40)
    if not appropriate_size:
        continue
        
    path = "/home/ssantiago/Descargas/dataset_artwork_PRUEBAS-SS/"
    # Nombre generico que luego será cambiado
    name = "image" + str(count_image_id)
    
    # Descargamos la imagen
    download_image(url_i, path, name)
    
    # Obtenemos el formato de la imagen
    extension = get_extension(path, name)
    
    # Variables para el JSON de la imagen que se acaba de descargar
    url = url_i
    hash = hash_file(path + name)
    
    # Le damos formato al image_id (6 digitos). Utilizamos zfill para rellenar el string con "0" hasta llegar a 6 digitos
    image_id = str(count_image_id)
    image_id = image_id.zfill(6)
    
    # Cargamos los valores al diccionario que luego será descargado en formato JSON
    dict_data_json = {
    "face_type": face_type,
    "fake_group": fake_group,
    "fake_type": fake_type,
    "fake_detailed_type": fake_detailed_type,
    "identified_person": identified_person,
    "url": url,
    "image_id": image_id,
    "operator_id": operator_id,
    "hash": hash,
    "bulk_id": bulk_id,
    "source": source
    }
    
    # Nuevo nombre para los archivos (se lo podemos poner ahora porque ya tenemos el dato del hash)
    new_name = f"b{bulk_id}-i{image_id}-unidentified-{source}-{operator_id}-{hash[-6:]}-origin"
    # Renombramos la imagen
    rename_file(path, name, new_name + extension)
    # Guardamos el diccionario como JSON con el mismo nombre pero diferente extension
    download_json(dict_data_json, path, new_name + ".json")
    
    # Incrementamos los contadores para la siguinte iteración
    count_image_id += 1
  
# Archivo para registrar la ejecución
execution_txt = f"bulk_id: {bulk_id}\nquery: {query}\nfake_group: {fake_group}\ndatetime: {datetime.now().strftime('%Y-%m-%d %H:%M')}\nuser: {operator_id}\ndownloads during the run: {count_image_id - 1}"
# Descargamos el archivo

path = "/home/ssantiago/Descargas/dataset_artwork_PRUEBAS-SS/ejecuciones/"
filename = f"b{bulk_id}-{source}-execution-{operator_id}.txt"
create_text_file(path, filename, execution_txt)
