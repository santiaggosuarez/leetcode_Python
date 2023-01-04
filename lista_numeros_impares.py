# Función para obtener los primeros 7 números impares después del 100
def lista_impares():
  lista = []
  num = 100

  while len(lista) < 7:
    if num % 2 != 0:
      lista.append(num)
    num += 1

  return lista

if __name__ == "__main__":
  print("PROBLEMA 2\nLista con los primeros 7 números impares después del 100:\n")
  print(lista_impares())
