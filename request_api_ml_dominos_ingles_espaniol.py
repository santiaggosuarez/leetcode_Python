import requests
import doctest

if __name__ == "__main__":

  # Creo la lista donde voy a guardar los dominios
  list_of_domains = []
  
  # Url sobre la que quiero trabajar
  url = "https://api.mercadolibre.com/catalog_domains/"
  
  # Me devuelve un objeto de tipo response
  response = requests.get(url)

  # Obtengo todos los json de response en formato de lista
  list_of_json = response.json()
  
  # Recorro y obtengo cada json (json tienen formato de diccionario)
  for i in list_of_json:

    # Obtengo id con la clave id
    get_id = i["id"]

    """# Trabajo sobre los CBT para obtener el dominio del "name" (en ingles)
    if get_id[:4] == "CBT-":
      # Obtengo y agrego los dominios ("name") a la lista correspondiente
      get_name = i["name"]
      list_of_domains.append(get_name)"""

    # Trabajo sobre los MLA para obtener el dominio en ingles y nombre en español
    if get_id[:4] == "MLA-":
      
      get_name = i["name"]

      # Normalizo el formato del dominio en ingles
      get_id = get_id.lower()
      get_id = get_id.replace("_"," ")
      get_id = get_id.replace("mla-","")
      get_id = get_id.capitalize()

      # Agrego el dominio en ingles y al lado el nombre en español
      list_of_domains.append(get_id + " - " + get_name)

    

  list_of_domains.sort()
  print(list_of_domains)

  # Guardar lista de dominios en un archivo txt
  """file = open("dominios.txt","w")
  for i in list_of_domains:
    file.write(i + "\n")
  file.close()"""

  """TEST
  >>>len(list_of_domains)
  5199
  """
  print("\n",doctest.testmod())

  #print(str(len(list_of_json)/21))
  print(len(list_of_domains))
