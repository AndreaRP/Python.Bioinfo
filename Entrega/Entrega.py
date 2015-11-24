#coding=utf-8
#Queremos almacenar los artículos que leemos en una BD , pero no nos gusta ninguna de las disponibles, por lo tanto vamos a
#construirla nosotros mismos. La BD será una lista de diccionarios. Cada diccionario consta de 5 campos: Título del artículo,
#autores, revista, fecha y nombre del fichero donde guardamos un resúmen del artículo.
#El programa nos permitirá hacer una serie de cosas elegidas por un menú:
# 1. Introducir un nuevo elemento, esto implicará salvarlo en un archivo
# 2. Listar todos los artículos, especificando los 4 primeros campos
# 3. Buscar si existe un artículo dando una palabra clave del artículo
# 4. Buscar si existe un artículo dando el nombre de un autor
# 5. Listar todos los artículos de una determinada revista
# Cada vez que se arranca el programa deberán recuperarse los datos almacenados previamente
articulos = []
atributos={}
def leerArchivo(file):
    origen = open(file)
    lineas = origen.readlines()
    for linea in lineas:
        propiedades = linea.split(';')

        atributos.update({'nombre':propiedades[0]})
        atributos.update({'autores':propiedades[1]})
        atributos.update({'revista':propiedades[2]})
        atributos.update({'fecha':propiedades[3]})
        atributos.update({'ruta':propiedades[4]})
        print(atributos)
        articulos.append(atributos)
        print(articulos)
    atributos.clear()
    origen.close()
    return articulos

articulos = leerArchivo('./articulos.txt')
opcion = raw_input("Indica una opción: ")
while opcion != 'exit':
    if opcion == '1':
        atributos.update({'nombre':raw_input('Indica el nombre: ')})
        atributos.update({'autores':raw_input('Indica los autores: ')})
        atributos.update({'revista':raw_input('Indica la revista: ')})
        atributos.update({'fecha':raw_input('Indica la fecha: ')})
        atributos.update({'ruta':raw_input('Indica la ruta: ')})
    elif opcion == '2':
        n=0
        for articulo in articulos:
            print(articulo)
            n+=1
            print(n)
            print('nombre: '+articulo['nombre'])
            print('autores: '+articulo['autores'])
            print('revista: '+articulo['revista'])
            print('fecha: '+articulo['fecha'])
    elif opcion == '3':
        clave=raw_input('Indica palabra clave: ')
        for articulo in articulos:
            for palabra in articulo['nombre'].split(' '):
                if palabra == clave:
                    print('Contienen la clave: '+articulo['nombre'])
    elif opcion == '4':
        buscoAutor=raw_input('Indica un autor: ')
        for articulo in articulos:
            for autor in articulo['autores'].split(','):
                if autor == buscoAutor:
                    print(autor+ ' ha escrito: '+articulo['nombre'])
    elif opcion == '5':
        revistaQuery=raw_input('Indica una revista: ')
        for articulo in articulos:
            if articulo['revista'] == revistaQuery:
                print(articulo['nombre'])
    opcion = raw_input("Indica una opción: ")