"""Hallar las raíces de f(x) = x^2 -x -2 usando la fórmula resolvente e imprimir los dos valores de x (como números enteros).
El output debería tener la siguiente forma:
x_1={raíz más chica}, x_2={raíz más grande}

Definir una variable para cada uno de los coeficientes a, b y c de la función f(x).
Vamos a usar la fórmula resolvente de las ecuaciones cuadráticas. Para hacerlo, definimos, primero, una variable para el discriminante (la parte de adentro de la raíz). Después, vamos a generar una variable para x_1 y otra para x_2, usando la ecuación resolvente (a una le corresponde la raíz positiva y a la otra la positiva). Redondeamos e imprimimos ambas, respetando el formato.
"""

import math

a = 1
b = -1
c = 2
cero = a**2 - b - c

discriminante = (b**2-4*a*c) *-1  # Multiplico por -1 para que la discriminante sea un número positivo, de otra forma no se puede calcular la raíz
raiz = math.sqrt(discriminante)

# Formula resolvente
x_1 = (-b + raiz) / (2*a)
x_2 = (-b - raiz) / (2*a)

raiz_mas_grande = round(x_1)
raiz_mas_chica = round(x_2)

print(f"x_1={raiz_mas_chica}, x_2={raiz_mas_grande}")
