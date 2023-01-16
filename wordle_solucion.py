wordle = "MUNDO"

def color_de_letra(letra, posicion_ingresada):
  global wordle
  color = ""

  if letra not in wordle:
    color = "GRIS"
  else:
    if letra == wordle[posicion_ingresada]:
      color = "VERDE"
    else:
      color = "AMARILLO"
  
  return color

def evaluar_colores(palabra_propuesta):
  lista_colores = []

  posicion = 0
  for letra in palabra_propuesta:
    color = color_de_letra(letra, posicion)
    posicion += 1
    lista_colores.append(color)

  return lista_colores
  
def informar_aciertos(palabra_propuesta):
  lista_colores = evaluar_colores(palabra_propuesta)
  string_con_formato = "-".join(lista_colores)

  print(f"El resultado de {palabra} es: {string_con_formato}")

lista_palabras = ["FUMAR", "MUNIR", "MUNIO", "MUNDO"]

for palabra in lista_palabras:
  informar_aciertos(palabra)
