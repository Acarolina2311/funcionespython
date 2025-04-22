def calculartiempodelecturadeexcel(filas,topelectura):
    tiempototal=0
    tiempototal = filas/topelectura
    if filas%topelectura != 0:
        tiempototal = tiempototal + filas%topelectura/topelectura
    print("el tiempo de demora es:", tiempototal)

    
def sumadedosnumeros(a,b):
    resultado = a+b
    return resultado
    
    
def saludar():
    print("hola bienvenidos")
    
def sumatresnumeros(num1,num2,num3):
    suma_2= sumadedosnumeros(num1,num2)
    print("el valor es:", suma_2)