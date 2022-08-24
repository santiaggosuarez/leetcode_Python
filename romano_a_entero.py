#Dado un número romano, conviértelo en un número entero.

def romano_a_int(romano):
  #convertimos parámetro a mayúsculas para no tener problemas de comparación
  #declaramos diccionario con los valores
  #declaramos variable int
  romano = romano.upper()
  valores_romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
  num = 0

  #chequeo que se ingresen valores romanos
  for letra in romano:
    if letra not in valores_romanos:
      print("Error en los valores ingresados.")
      return "NaN"

  #conseguir numero romano
  for i in range(len(romano)):
    #con i > 0 nos aseguramos que siempre sume el primer valor
    #si el valor siguiente es mayor al anterior entonces restamos (ejemplo IX = 9)
    if i > 0 and valores_romanos[romano[i]] > valores_romanos[romano[i-1]]:
      #operación matemática para asegurar que siempre se reste el valor necesario
      num += valores_romanos[romano[i]] - (2 * valores_romanos[romano[i-1]])

    #si el valor siguiente es menor entonces sumamos (ejemplo XI = 11)
    else:
      num += valores_romanos[romano[i]]

  return num

print("CONVERTIR ROMANO A ENTERO")
x = input("Romano: ")
print("Entero: ", romano_a_int(x))
