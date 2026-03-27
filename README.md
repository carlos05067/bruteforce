## ¿Cómo ejecutar el programa?
1. Tener instalado matplotlib
2. Ejecutar el script: python bruteforce.py

## Ejemplos de salida
Probando contraseñas: abgo
Probando contraseñas: abgp
Probando contraseñas: abgq
Probando contraseñas: abgr
Contraseña encontrada: abgr
Total de intentos: 49518
Tiempo de ejecución: 4.40 segundos

## Reflexión
Si la contraseña tiene 8 o más caracteres y usa mayúsculas, números
y símbolos el total de combinaciones
sería, 95^8 = 6,634,204,312,890,625. Nos demorariamos mas 76 días en el peor caso.
Lo que significa que las contraseñas largas y con varios signos, son las mas robustas
y dificiles de desifrar por este metodo.
