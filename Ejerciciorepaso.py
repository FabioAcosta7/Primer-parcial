"""Ejercicio de repaso"""

print('dame tu primera nota')
g1 = input()
print('dame tu segunda nota')
g2 = input()
print('dame tu tercera nota')
g3 = input()

promedio = ((int(g1) + int(g2) + int(g3))/ 3)
print("aprobado" if promedio >= 5 else "reprobado")
print(promedio)
