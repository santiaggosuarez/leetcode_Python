# Función para saber si un número es primo
def es_primo(num):
  for i in range(2,num):
    if num % i == 0:
      return False
  return True

# Función para saber si un número termina en 1
def termina_en_uno(num):
  num_str = str(num)
  return num_str[-1] == "1"

# Función para imprimir los números primos que terminen en 1 en un intervalo dado por parámetro
def imprimir_primos(desde,hasta):
  for i in range(desde,hasta+1):
    if es_primo(i) and termina_en_uno(i):
      print(i)

if __name__ == "__main__":
  print("PROBLEMA 4\nImprimir los números primos desde 1 a 10.000 que terminen en 1:\n")
  imprimir_primos(1,10000)
