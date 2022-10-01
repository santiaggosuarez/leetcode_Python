# Imprimir en pantalla, cada 10 números, "los números entre x y x+9 son:" x, x+1, x+2, ..., x+9, entre el 1 y el 100. O sea, el programa debe imprimir lo siguiente:
#Los números entre 1 y 10 son: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#Los números entre 11 y 20 son: 11, 12, ..., 19, 20 Los números entre 21 y 30 son: 21,..., 30
#Los números entre 91 y 100 son: 91, 92..., 99, 100

def imprimir_cada():
  # Recorro los números del 1 al 100 cada 10
  for i in range(1,100,10):
    print(f"Los números entre {i} y {i+9} son:", end=" ")

    # Imprimo cada uno de los números dentro de ese recorrido
    for k in range(i,i+10):
      if k < i+9:
        print(k, end=", ")
      else:
        print(k, end="\n")

      # Utilicé el 'end=' dentro del 'print' para darle el formato pedido en la consigna

if __name__ == "__main__":
  print("PROBLEMA 5\nImprimir en pantalla, cada 10 números, 'los números entre x y x+9 son:' x, x+1, x+2, ..., x+9, entre el 1 y el 100:\n")
  imprimir_cada()
