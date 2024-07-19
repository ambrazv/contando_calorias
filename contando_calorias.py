# El programa debe solicitar al usuario la cantidad de gramos de proteína, carbohidratos y grasa; calcular las calorías usando la fórmula \( \text{calorías} = 4 \times (\text{proteína} + \text{carbohidratos}) + 9 \times \text{grasa} \); redondear las calorías hacia arriba, y finalmente imprimir el resultado en el formato: "Las calorías totales del producto son: <calorías redondeadas>".

import math

 # Solicitar al usuario la informacion

proteina = float(input( "Ingrese las proteinas:\n>")) #1.9
carbohidratos = float(input( "Ingrese los carbohidratos:\n>")) # 9 .2
grasa = float(input( "Ingrese el de la grasa:\n>")) # 7

#calcular las calorias
calorias = 4 * (proteina + carbohidratos) + 9 * grasa
calorias = math.ceil(calorias)

# mostrar resultados
print ("Las calorias totales del producto son: {calorias}")