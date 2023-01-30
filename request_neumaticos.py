import requests

if __name__ == "__main__":

  # Dirección que quiero consultar
  url = "https://api.mercadolibre.com/sites/MLC/searchbackend?q=neumaticos"
  
  # Variable para guardar los datos que consulté
  data = requests.get(url)
  
  # Listas donde voy a guardar lo que me interesa extraer
  list_result_ids = []
  list_permalink = []
  list_titles = []
  
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
      list_permalink.append(data["permalink"])
      list_titles.append(data["title"])
          
  
  # Esta linea convierte dos listas a diccionario, no la uso por el momento
  dict_ids_and_permalink = dict(zip(list_result_ids, list_permalink))
  
  # Imprimo cada dato en las listas separados por comas para copiarlo en formato csv
  for id, link, title in zip(list_result_ids, list_permalink, list_titles):
    print(id, link, title, sep=",")
