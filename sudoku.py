from pickle import TRUE
#Insert your code below this line

tablero_1 = {
    "fila_1" : [1,2,3,4],
    "fila_2" : [2,3,4,1],
    "fila_3" : [3,4,1,2],
    "fila_4" : [2,4,1,3]
}

def conjunto_cumple_con_requisitos(conjunto):
  lista_numeros = [1,2,3,4]
  for numero in lista_numeros:
    if conjunto.count(numero) != 1:
      return False
  return True

def obtener_columna(tablero, numero_columna):
  columna = []
  for fila in tablero:
    numero_a_obtener = fila[numero_columna]
    columna.append(numero_a_obtener)
  return columna

dic_coordenadas_bloques = {
    1:{tuple([n°_fila_1, n°_fila_2]):[n°_columna_1, n°_columna_2]}
    2:
    3:
    4:
}

def obtener_bloque():
