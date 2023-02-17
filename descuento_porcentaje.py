"""En una tienda online de ropa, si tu compra supera los 5000, recibís un descuento del 5%. Escribir el código simplificado e imprimir cuánto debe abonar finalmente una persona que gasta 7000. El output es solo el número, sin signo de pesos, y redondeado a dos decimales."""

importe = 7000
umbral = 5000

descuento = 0.05 if importe > umbral else 0

importe_final = round(importe * (1 - descuento), 2)

print(importe_final)
