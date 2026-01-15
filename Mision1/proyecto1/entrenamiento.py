# librerías
import re
"""
Espresiones regulares en Python
Problemas Reales 
"""
#Codigo
print("Librería cargada correctamente")
# Ejemplo1
texto="Mi Número es 12345"
resultado=re.search(r"\d+",texto)
print(f"{texto} Resultado {resultado.group()}")   
texto="Mi Número es 12345-985"
resultado=re.search(r"\d+",texto)
print(f"{texto} Resultado {resultado.group()}")   
  