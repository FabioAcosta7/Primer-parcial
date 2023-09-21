"""Cod_olimpiadas"""
def multiplicacion(a,b):
  x = a*b
  return x

def division(a,b):
  x = a/b
  return x

print("dame el primer numero:")
a = int(input())
print("dame el segundo numero:")
b = int(input())
print("la multiplicación de a y b es:", multiplicacion(a,b), "y la división es", division(a,b))

def area_triangulo(base,altura):
  x = (base*altura)/2
  return x

print("dime cuanto mide la base:")
base = (int(input()))
print("dime cuanto mide la altura:")
altura = (int(input()))
print("el area de su triangulo es:", area_triangulo(base,altura))

def conversion(kilometros):
  x = kilometros*1000
  return x

print("Cuantos kilometros usted ha recorrido")
kilometros = (int(input()))
print("La cantidad en metros es:", conversion(kilometros))
