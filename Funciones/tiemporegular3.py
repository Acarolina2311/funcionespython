import funcionregular

filas=790
topelectura=100

funcionregular.saludar()

funcionregular.calculartiempodelecturadeexcel(filas,topelectura)

def saludar2():
    print("hola a todos")

def invertir_numero(numero):
    invertido = 0
    while numero > 0:
        invertido = invertido * 10 + (numero % 10)
        numero = numero // 10
    return invertido

# Prueba
clave = 875964
print("Número original:", clave)
print("Número invertido:", invertir_numero(clave))