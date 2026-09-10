######Examen Recuperatorio Python 
#Tema:Matrices
#año: 3año 
#Modalidad Informatica
#Nombre: Augusto 
#Apellido: Correa
#Fecha: 10/09/26









matriz = []
 
while True:
    print("1. Carga la matriz")
    print("2. Mostrar la matriz")
    print("3. Sumatoria")
    print("4. Productoria")
    print("5. Transpuesta")
    print("6. Salir")
    opcion = int(input("Elegí una opción: "))

    if opcion == 1:
        matriz = []
        filas = int(input("Cantidad de filas: "))
        columnas = int(input("Cantidad de columnas: "))
        for y in range(filas):
            fila = []
            for z in range(columnas):
                valor = int(input("ingrese un valor: "))
                fila.append(valor)
                matriz.append(fila)

    elif opcion == 2:
        for fila in matriz:
            print(fila)

    elif opcion == 3:
        suma = 0
        for fila in matriz:
            for valor in fila:
                suma += valor
        print("La sumata de la matriz es (redobleo de tambor):", suma)

    elif opcion == 4:
        producto = 1
        for fila in matriz:
            for valor in fila:
                producto *= valor
        print("La productoria de la matriz es| (gritos de la gente obacionando a esta respuesta):", producto)

    elif opcion == 5:
        transpuesta = []
        for y in range(len(matriz[0])):
            fila_transpuesta = []
            for epstein in range(len(matriz)):
                fila_transpuesta.append(matriz[epstein][y])
            transpuesta.append(fila_transpuesta)
        print("La matriz transpuesta es:")
        for fila in transpuesta:
            print(fila)

    elif opcion == 6:
        print("Acabando en el programa, digo cerrando el programa jajaja (nico tomatelo de chiste)")
        break
    

        