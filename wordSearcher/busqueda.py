import time

#Abrir archivo
archivo = open('archivoNuevo.txt', 'r')

#Leer todo el archivo
lineas = archivo.read()

#Cierro el archivo
archivo.close()

#Separo las palabras
palabras = lineas.split()

startTime = time.time()
#Definicion de la funcion busqueda
def busquedaBinaria(lista, buscar, menor, mayor):
    if menor > mayor:
        return -1
    
    mitad = (menor + mayor) // 2
    if buscar == lista[mitad]:
        return mitad
    elif (buscar < lista[mitad]):
        return busquedaBinaria(lista, buscar, menor, mitad - 1)
    else:
        return busquedaBinaria(lista, buscar, mitad + 1, mayor)

palabraBuscar = 'worst'
posicion = busquedaBinaria(palabras, palabraBuscar, 0, len(palabras) - 1)
if not posicion == -1:
    print("La palabra", palabraBuscar, "esta en la posicion :", posicion)
else:
    print("La palabra no se ha encontrado")

endTime = time.time()
totalTime = endTime - startTime
print("El tiempo de la busqueda fue de:", totalTime, "segundos")

