# Borges es uno de los más grandes escritores del siglo pasado. En su carrera, escribió cuentos, poesías y ensayos, principalmente. La cantidad de cuentos que produjo puede listarse, por libro y cronológicamente, de la siguiente manera:

# -Historia universal de la infamia (1935): 14 cuentos
# -Ficciones (1944): 17 cuentos
# -El Aleph (1949): 17 cuentos
# -El informe de Brodie (1970): 11 cuentos
# -El libro de arena (1975): 13 cuentos
# -La memoria de Shakespeare (1983): 4 cuentos

# Borges termina por quedarse ciego en 1955. Imprimí cuántos cuentos escribió antes y después de perder la vista. El output debe expresarse como:

# Antes de perder la vista, Borges escribió {cuentos previos} cuentos, y después {cuentos posteriores}

books_dict = {1944: ["Ficciones", 17],
              1949:["El Aleph", 17],
              1970:["El informe de Brodie", 11],
              1975:["El libro de arena", 13],
              1983:["La memoria de Shakespeare", 4]}

before_blindness = 0
after_blindness = 0
year_blindness = 1955

for book in books_dict:
  # Obtengo los datos del libro y guardo su cantidad de cuentos
  book_data = books_dict.get(book)
  number_of_tales = book_data[1]

  if book > year_blindness:
    after_blindness += number_of_tales
  else:
    before_blindness += number_of_tales

print(f"Antes de perder la vista, Borges escribió {before_blindness} cuentos, y después {after_blindness}")
