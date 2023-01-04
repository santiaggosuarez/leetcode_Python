"""Trabajás para una central de inteligencia y te encargan la tarea de descifrar un mensaje encriptado que interceptaron a una organización criminal. Por suerte, ya sabés cuál es el método de encriptado. El mismo consta de tres pasos. Para entender su funcionamiento, veamos cómo quedaría encriptada la frase "top secret".

1) Convertir todos los caracteres a mayúsculas:
secret -> SECRET
2) Reflejar la palabra:
SECRET -> TERCES
3) Concatenar la palabra tres veces:
TERCES -> TERCESTERCESTERCES

Tu tarea es realizar un programa que desencripte los mensajes de la organización criminal. En particular, imprimir el mensaje oculto detrás de "ASERPROSASERPROSASERPROS" sabiendo que es un código de una palabra en minúscula. El output debería ser:

El mensaje desencriptado es "{mensaje desencriptado}""""

encrypted_message = "ASERPROSASERPROSASERPROS"

# Función para reflejar una palabra
def reverse(string):
  return string[::-1]

# Función para "deconcatenar" una palabra (toma como argumento la cantidad de veces que se repite dicha palabra)
def deconcatenate(string, replay):
  deconcatenate_size = round( len(string) / replay )
  deconcatenate_string = string[0 : deconcatenate_size]
  return deconcatenate_string

# Función para desencriptar
def decryptor(message):
  # Paso el mensaje a minusculas, deconcateno, reflejo y retorno el mensaje
  message = message.lower()
  message = deconcatenate(message, 3)
  message = reverse(message)
  return message
  
decrypted_message = decryptor(encrypted_message)

print(f'El mensaje desencriptado es "{decrypted_message}"')
