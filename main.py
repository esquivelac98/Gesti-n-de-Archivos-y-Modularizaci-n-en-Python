# Proyecto: 
# Estudiante: Kevin Esquivel Acuña
# Fecha de Inicio: 2025/02/04
# Fecha de Entrega: 
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

from analisis_datos.estadisticas import media, calcular_mediana

lista_parametro = [5,3,1,2,4,8]

print('Media: ', round(media(lista_parametro), 2))
print('Mediana: ', round(calcular_mediana(lista_parametro), 2))



from analisis_datos import *

lista_compras = generar_lista_de_compras()