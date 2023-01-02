"""Los científicos consideran que el origen de la Tierra fue hace 4,543 miles de millones años. En cambio, el surgimiento de los mamíferos se remontaría a unos 2,00 millones de años. Si representamos la historia de la Tierra como un reloj, cuyas 0 hs coincide con en el origen del planeta y las 24 hs con la actualidad, imprimir a qué hora la Tierra empezó a ser habitada por mamíferos (redondear a un número entero). El output debe expresarse como:

La Tierra ha estado habitada por mamíferos desde las {hora de inicio} hs"""

origin_of_earth = 4.543
origin_of_mammals = 0.2
origin_of_mammals_in_relation_origin_of_earth = origin_of_earth - origin_of_mammals

# Regla de tres simple
start_time = (origin_of_mammals_in_relation_origin_of_earth * 24) / origin_of_earth

start_time = round(start_time)

print(f"La Tierra ha estado habitada por mamíferos desde las {start_time} hs")
