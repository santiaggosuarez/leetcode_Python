"""En un bolillero, hay bolas numeradas del 3 al 17. Imprimir cuál es la probabilidad de sacar un número par menor a 11. Expresar el resultado con dos decimales."""

def es_par(numero):
  return numero % 2 == 0

bolillero = list(range(3,18))
nro_favorables = 0
nro_no_favorables = 0

for bola in bolillero:
  if bola < 11 and es_par(bola):
    nro_favorables += 1
  else:
    nro_no_favorables += 1

total = nro_favorables + nro_no_favorables
probabilidad = round( nro_favorables / total, 2 )

print(probabilidad)
