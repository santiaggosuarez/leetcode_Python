# Función para imprimir los múltiplos de dos cifras de un número dado por parámetro
def multiplos_de(num):
  for i in range(10,100):
    if i % num == 0:
      print(i)

if __name__ == "__main__":
  print("PROBLEMA 3\nImprimir los múltiplos de 7 de dos cifras:\n")
  multiplos_de(7)
