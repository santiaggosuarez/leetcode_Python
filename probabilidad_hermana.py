"""En tu familia hay cuatro hermanos: 3 varones y 1 mujer. Vos, que sos la mujer, hubieras preferido tener una hermana. Siempre creíste que el hecho de no tener ninguna es una prueba matemática irrefutable de que el Universo te detesta. Ahora, que tenés conocimientos de programación, decidís terminar de demostrarlo. Imprimir cuál es la probabilidad (como un número decimal con dos cifras significativas) de que, al nacer 4 personas, solo 1 sea mujer.
El output debería ser:

La probabilidad de no tener hermanas es de {probabilidad}"""

posibles_sexos = ["m","f"]
combinaciones_totales = 0
combinaciones_favorables = 0

for i in posibles_sexos:
  combinacion_1 = i
  for j in posibles_sexos:
    combinacion_2 = combinacion_1 + j
    for k in posibles_sexos:
      combinacion_3 = combinacion_2 + k
      for l in posibles_sexos:
        combinacion_4 = combinacion_3 + l

        cont_letra_f = 0
        for letra in combinacion_4:
          if letra == "f":
            cont_letra_f += 1
        
        if cont_letra_f == 1:
          combinaciones_favorables += 1
        
        combinaciones_totales += 1

probabilidad = round( combinaciones_favorables / combinaciones_totales, 2 )

print(f"La probabilidad de no tener hermanas es de {probabilidad}")
