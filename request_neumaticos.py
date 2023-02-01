import requests

def get_data(site, query):
  # Dirección que quiero consultar
  url = f"https://api.mercadolibre.com/sites/{site}/searchbackend?q={query}"
  
  # Variable para guardar los datos que consulté
  data = requests.get(url)
  
  # Listas donde voy a guardar lo que me interesa extraer
  list_result_ids = []
  list_permalink = []
  list_titles = []
  list_tire_size = []
  list_rim_diameter = []
  
  # Si la página no está caída sigo realizando consultas (si da 400 por ej es ERROR)
  if data.status_code == 200:
    # Convierto los datos a json (para trabajar con formato de diccionario)
    data = data.json()
  
    # Extraigo la información que me interesa, en este caso, los results_ids
    for id in data["result_ids"]:
      # Agrego la información a la lista correspondiente
      list_result_ids.append(id)
  
  
  # Por cada results_id que obtuve, voy a buscar la información que necesite
  for id in list_result_ids:
    # Ingreso a la información del item con el results_id en la api de items
    url = "https://api.mercadolibre.com/items/" + id
    data = requests.get(url)
  
    if data.status_code == 200:
      data = data.json()
  
      # Obtengo la información que quiero y la agrego a la lista correspondiente
      permalink = data["permalink"]
      title = data["title"]
      list_permalink.append(permalink)
      list_titles.append(title)

      attributes = data["attributes"]
      bool_check_size = True
      for att in attributes:
        if att["id"] == "MANUFACTURER_TIRE_SIZE":
          bool_check_size = False
          size = att["value_name"]
          list_tire_size.append(size)
      if bool_check_size:
        list_tire_size.append("None")

      attributes = data["attributes"]
      bool_check_rim = True
      for att in attributes:
        if att["id"] == "RIM_DIAMETER":
          bool_check_rim = False
          rim = att["value_name"]
          list_rim_diameter.append(rim)
      if bool_check_rim:
        list_rim_diameter.append("None")
          
  
  # Esta linea convierte dos listas a diccionario, no la uso por el momento
  dict_ids_and_permalink = dict(zip(list_result_ids, list_permalink))
  
  # Imprimo cada dato en las listas separados por comas para copiarlo en formato csv
  print(query)
  for id, link, title, size, diameter in zip(list_result_ids, list_permalink, list_titles, list_tire_size, list_rim_diameter):
    print(query, id, link, title, size, diameter, sep=",")
  print("-----","-----","-----","-----","-----","-----", sep=",")
  

if __name__ == "__main__":

  get_data("MLC","NEUMATICOS")
