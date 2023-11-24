#Diego Maldonado
#Actividad 05

#Abrir archivo
archivo = open('Dracula.txt', encoding='utf-8')

#Leer todo el archivo
lineas = archivo.read()

#Cierro el archivo
archivo.close()

#Separo las palabras
palabras = lineas.split()

#lista con palabras en minuscula para organizar mejor
listaPalabras = []
for i in palabras:
    listaPalabras.append(i.lower())

#Funcion para filtrar las palabras
def PalabrasUnicas(lista):
    palabrasSinRepetir = []
    for i in lista:
        if i not in palabrasSinRepetir:
            palabrasSinRepetir.append(i)
    return palabrasSinRepetir

palabrasReducidas = PalabrasUnicas(listaPalabras)
#print (palabrasReducidas)

#Funcion merge sort a utilizar
def mergeSort(lista):
    #Si la lista tiene menos de un elemento no se puede ordenar
    if len(lista) > 1:
        #La division izquierda va del inicio hasta la mitad
        lista_izquierda = lista[:len(lista)//2]
        #La division derecha va desde la mitad hasta el final
        lista_derecha = lista[len(lista)//2:]

        #recursividad
        mergeSort(lista_izquierda)
        mergeSort(lista_derecha)

        #mergear
        i = 0 #posicion de la lista izquierda
        j = 0 #posicion de la lista derecha
        k = 0 #posicion de la lista mergeada
        while i < len(lista_izquierda) and j < len(lista_derecha):
            if lista_izquierda[i] < lista_derecha[j]:
                lista[k] = lista_izquierda[i]
                i += 1
            else:
                lista[k] = lista_derecha[j]
                j += 1
            k += 1
        
        while(i < len(lista_izquierda)):
            lista[k] = lista_izquierda[i]
            i += 1
            k += 1

        while (j < len(lista_derecha)):
            lista[k] = lista_derecha[j]
            j += 1
            k += 1

#Ordenar las palabras
mergeSort(palabrasReducidas)

with open('archivoNuevo.txt', 'w') as archivo:
    for i in palabrasReducidas:
        archivo.write(i + " ")