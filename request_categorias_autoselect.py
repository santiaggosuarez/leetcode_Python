import requests
import doctest

# Lista de id de las categorias obtenidos a partir de la planilla (se descargaron las filas en formato csv para que aparezcan separados por comas)
list_categ_id = [30083,30084,14555,14548,433729,412694,14548,14555,14548,30099,14555,416711,14555,11034,14555,14548,1618,14555,14548,1593,14548,0,14555,30084,1593,14548,411920,1631,30083,30083,14548,416711,14548,30084,378163,11034,11034,0,14548,391516,14555,48895,14548,30083,392282,412694,412694,14555,1593,30099,30084,1593,1593,1618,1574,14548,416711,14548,14555,74543,412694,30040,14555,1593,31032,14555,14548,14548,1593,30099,14555,1593,435264,11034,392282,414083,14548,14555,401912,1593,1624,14555,413527,14548,30099,14555,14548,14555,1368,412694,11034,30040,0,30083,34263,14555,0,14548,14555,14555,30082,392282,0,14548,48888,14548,378163,401912,30040,1631,0,0,30084,30084,30083,14548,14548,0,14555,455586,14555,14548,0,14548,29914,413527,14548,1624,48895,392282,14548,1574,48888,1593,14548,0,14548,30083,34263,1631,0,30084,14555,14555,30084,433729,416711,14555,14548,0,14548,14548,14555,30084,1574,1368,30083,432923,14559,14555,433729,30084,14548,0,0,14555,378163,14555,1368,74531,14548,30083,14548,1740,416711,30098,14555,1574,14548,1616,1500,11034,1624,14548,14555,1624,436289,14548,30098,0,14548,413527,14548,1593,0,14555,0,14548,0,372115,14555,432923,14548,14548,30098,455755,14555,1624,1616,1624,74528,1584,391077,30974,5411,14548,14555,14555,14555,416711,14555,30040,30083,34263,48888,1593,1593,5411,30083,372115,14555,30083,14555,412694,4623,0,14548,30083,441112,14555,14548,29914,14548,433729,14548,0,48895,30084,14555,14555,0,30099,14548,14548,48888,412694,1593,30099,14555,30084,1593,391516,0,30083,0,1574,14548,0,412694,14548,1500,14548,14555,433729,14548,14555,372119,0,1500,378163,14555,14548,30099,34263,1624,1592,14548,1624,372119,30083,14548,14555,412694,5726,14555,0,1631,372115,412694,392282,1631,14555,14555,1631,0,435264,14548,30040,372115,4621,14548,4854,407134,0,30040,30083,0,14555,1593,1624,30084,0,14555,14548,14548,30084,1368,14548,14548,14548,14555,1592,436289,74531,14555,14548,392282,373499,14555,1592,30974,407134,30099,14548,30083,432923,14555,30084,14555,14555,14548,14555,1631,1624,412620,14548,407134,14555,14548,14555,1616,380652,0,0,14555,1631,14555,401912,436289,14555,14548,414075,14555,412694,0,432923,14548,412694,0,14555,14555,14555,391077,14555,5411,412694,1593,74543,1593,407134,78318,14555,0,30084,29914,30084,5411,14548,1593,14555,1593,412694,14548,14555,14555,391077,14548,1618,14555,1593,411920,412694,30084,0,412694,435264,1368,1574,30084,1593,0,29884,14548,14555,0,1631,14555,412621,0,1500,407134,14555,34263,14555,432923,432923,0,14548,30098,1368,412620,34263,14555,14548,1368,1624,30083,372119,1592,14555,30082,14548,0,14555,412694,30040,14548,0,0,0,5235,1592,14548,14555,30974,372115,29914,30084,31032,0,0,14555,30099,14555,432923,14555,48888,14548,14555,14555,30084,4854,407134,1631,14548,1593,0,435264,30084,416711,1368,30099,30084,1593,438142,14555,14555,372119,1631,14548,416711,30099,0,14548,1368,30084,0,14548,14548,14555,14548,413524,30084,436289,411920,14555,14555,1500,4621,1500,14555,14555,0,14548,30083,1071,1624,14555,14548,30083,14555,0,372115,14548,9972,433729,74537,14555,407134,0,401912,14555,14559,412694,14548,0,1574,0,14555,11034,14548,31032,412585,0,1592,436289,14548,30084,1500,0,30084,1593,1368,14559,1368,1593,413524,14548,48895,14555,14555,1574,1616,372119,14555,30099,14548,14555,5235,1624,14548,14555,14548,30083,30084,407134,14555,0,14555,1584,14548,412694,433729,14548,0,29914,74528,1593,14548,1574,14548,1592,14548,1584,14555,403697,1246,433729,14548,372006,14555,0,412694,14548,14548,1500,14548,14555,14548,412585,14555,14555,392282,413451,0,74531,0,30084,30098,412694,1584,14555,11034,14548,1616,14555,0,48888,1574,429026,1592,14548,0,0,14548,47540,433729,0,5976,1574,413234,14548,438142,14548,1500,417845,14548,14555,4854,14555,1624,14555,14555,14555,14548,117185,14555,433729,30082,14548,1740,433729,14548,14548,1574,392282,14548,14555,0,14555,14548,378163,14548,14555,401912,30099,441112,14548,432923,0,9972,416711,48888,1592,30083,14548,14555,14548,11034,14548,30083,30084,14555,14555,413234,30084,11034,29914,401912,14555,14555,0,454695,30084,412687,14548,1500,1588,34263,14555,0,391516,14555,14555,14555,1500,30099,0,30084,30099,0,11034,412694,413234,416711,1500,0,74528,117185,1574,14548,1593,14548,413527,14548,1368,1593,14555,14548,14548,14548,1593,14555,69567,30084,14555,1593,412585,14548,14555,0,1500,14555,2676,30099,14555,30083,14559,14555,1592,30083,416711,30099,14548,14548,14548,14548,14548,1618,412694,14555,14555,14548,30084,0,14555,14555,0,1616,30083,14555,0,31032,30084,14548,14555,30083,1593,14555,14548,432923,1500,1500,14548,30098,433729,14548,14548,373499,391516,412694,0,1593,14548,0,0,14548,14548,9181,14555,48888,14548,14548,14555,416585,1574,321227,0,414075,14548,30084,14555,416711,30084,433729,14548,413234,1574,416711,31034,14555,14548,11034,14555,30084,14555,30084,14555,1632,455755,443024,11034,14548,391077,14548,14548,14555,14555,1584,14548,14548,0,14555,11034,30083,1593,14548,14555,34263,436298,433729,14555,30083,14555,14548,401912,378163,14555,48895,1593,14548,417668,0,412694,47540,0,412694,411944,1624,14555,14548,30084,1368,14548,413527,31032,387931,29914,1593,0,30083,436289,14555,14548,11034,30082,14548,0,14555,14555,14555,1574,14548,417668,1592,14555,30084,0,14548,401912,0,0,1593,14548,14555,30084,1624,1593,1500,14548,14548,14555,1593,372115,14555,0,0,392282,412694,1584,14548,30083,380652,1592,0,14555,14548,14548,1621,1624,0,117259,0,14548,14555,1071,14555,14548,401998,14548,14548,14555,1624,14548,1592,1368,1631,403697,14555,14555,14555,30084,1621,14548,14555,14555,388858,1616,14555,14555,14555,1592,0,438142,14555,10115,14548,1631,0,14548,0,0,0,1613,373499,14548,14555,0,436289,14555]

# Listas donde voy a guardar lo que me interesa extraer
list_categ_name = []

for id in list_categ_id:
  site = "MLA"
  categ_id = id

  # Los ids 0 (null) no tienen nombre
  if id == 0:
    list_categ_name.append("null")

  else:
    # Dirección que quiero consultar
    url = f"https://api.mercadolibre.com/categories/{site}{categ_id}"

    # Variable para guardar los datos que consulté
    data = requests.get(url)

    # Si la página no está caída sigo realizando consultas (si da 400 por ej es ERROR)
    if data.status_code == 200:
      # Convierto los datos a json (para trabajar con formato de diccionario)
      data = data.json()

      # Extraigo la información que me interesa, en este caso, los "name"
      name = data["name"]
      # Agrego la información a la lista correspondiente
      list_categ_name.append(name)

# Imprimo los nombres con saltos de linea para llevarlos directamente a la planilla
for name in list_categ_name:
  print(name)

"""
Test
>>> len(list_categ_id) == len(list_categ_name)
True
"""
print(doctest.testmod())