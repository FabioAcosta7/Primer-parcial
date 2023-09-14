"""Coding rush"""
import random
def funcion_dinero():  
  numero_aleatorio = random.randint(1, 100)
  print("seran", numero_aleatorio, "pesos")
  billete = input()
  cambio = int(billete) - numero_aleatorio
  print("su cambio es", cambio)
funcion_dinero()
