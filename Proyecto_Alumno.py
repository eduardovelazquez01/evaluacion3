#Programa en Python para poder conocer la información del alumno

print("¡Bienvenido a KuepiAlumno!")

#Definimos las funciones que necesitamos

def calcular_promedio(notas):
    if notas:
        promedio = sum(notas) / len(notas)
        return round(promedio,1)
    else:
        return 0

#En esta funcion implemente la funcion "round", me permite tomar el solo el primer dígito despúes del punto décimal.


def evaluar_promedio(promedio):
    if promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"

def obtener_estado_civil(codigo_estado):
    estados_civiles = {
        1: "Soltero",
        2: "Casado",
        3: "Divorciado",
        4: "Viudo"
    }
    return estados_civiles.get(codigo_estado, "No fué indicado")

def imprimir_datos_alumno(nombre,edad, promedio, estado_civil, evaluacion_promedio):
    print("Datos del Alumno")
    print("* Nombre del Alumno:", nombre)
    print("* Edad del Alumno:", edad)
    print("* Promedio general:", promedio)
    print("* Estado civil del alumno:", estado_civil)
    print("* Evaluación del promedio:", evaluacion_promedio)

def general():
    nombre = input("Ingrese el nombre del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    cantidad_notas = int(input("Ingrese la cantidad de notas del alumno: "))
    notas = []
    for num in range(cantidad_notas):
        nota = float(input(f"Ingrese la nota {num + 1}: "))
        notas.append(nota)

    promedio = calcular_promedio(notas)
    evaluacion = evaluar_promedio(promedio)
    codigo_civil = int(input("""Estados civiles:
1- Soltero
2- Casado
3- Divorciado
4- Viudo
Ingrese el estado civil del alumno: """))
    estado_civil = obtener_estado_civil(codigo_civil)
    imprimir_datos_alumno(nombre, edad, promedio,estado_civil, evaluacion)

general()