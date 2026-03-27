import itertools
import time
import matplotlib.pyplot as plt
 
alfabeto= "abcdefghijklmnopqrstuvwxyz0123456789"
contraseña= "abgr"   
 
def fuerza_bruta(contra: str, alfa: str):
    intentos= 0
    inicio= time.time()
    longitud= 1  
    while True:
        for combinacion in itertools.product(alfa, repeat=longitud):
            intento= "".join(combinacion)  
            intentos+= 1
            print(f"Probando contraseñas: {intento}")

            if intento== contra:
                fin= time.time()
                return intento, intentos, fin - inicio
        longitud+= 1  

encontrada, total_intentos, tiempo_total = fuerza_bruta(contraseña, alfabeto)
print(f"Contraseña encontrada: {encontrada}")
print(f"Total de intentos: {total_intentos:}")
print(f"Tiempo de ejecución: {tiempo_total:.2f} segundos")

"""Parte de la gráfica"""
longitudes = list(range(1, 6))
intentos_grafica = [sum(len(alfabeto) ** l for l in range(1, n + 1)) for n in longitudes]
colores = ["red" if l == len(contraseña) else "steelblue" for l in longitudes]

plt.plot(longitudes, intentos_grafica)
plt.scatter(longitudes, intentos_grafica, color=colores, zorder=5)
plt.xlabel("Longitud de la contraseña")
plt.ylabel("Número de intentos")
plt.title("Fuerza bruta: intentos vs longitud")
plt.savefig("grafica_fuerza_bruta.png")
plt.show()