#1) Revisa los siguientes códigos, impleméntalos e identifica el error.

def factorial(n):
    if n == 0:
        return 1
    else
        return n * factorial(n-1)
print(factorial(5))

# En la condicional "else", le hace faltan los dos puntos :
#------------------------------------------------------------------------------------------------#

numeros = [1,2,3,4,5]
for num in numeros
    print(num)

#En el ciclo for, al final le hace falta los dos puntos :
#------------------------------------------------------------------------------------------------#

def saludar(nombre):
    print("Hola" + nombre)
saludar("Alice", "Bob")

#Al establecer la función saludar, solo ponemos un solo parámetro donde puede ir un solo nombre
#pero al usar la funcion hay dos nombre como parámetros.
#------------------------------------------------------------------------------------------------#

num1 = 5
num2 = 10
suma = num1 + num2
print("La suma es: ", suma))

#Al imprimir por pantalla, hay dos parentesis al final, cuando realmente solo debria haber una
#------------------------------------------------------------------------------------------------#

def calcular_promedio(notas):
    suma = 0
    for nota in notas:
        suma += nota
    promedio = suma /len(notas)
    return promedio

notas_alumno = [85,92,78,95]
promedio = calcular_promedio(notas_alumno)
print("El promedio es:", promedio

#En este caso al imprimir por pantalla el promedio del alumno, en la ultima linea, le hace falta cerrar el paréntesis

