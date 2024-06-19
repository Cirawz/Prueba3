
import csv
lista = []

def cambio_nombre(a):
    for x in lista:
        if a == x[0]:
            print ("ID: ",x[0],"\nEquipo: ",x[1], "\nPuntos: ",x[2])
            nuevo_nombre = input("Ingrese nuevo nombre: \n")
            for x in lista:
                print("algo")
def estadisticas()
    cont=0
    acum=0
    for x in lista:
        cont = cont+1
        acum=int(acum+x[2])
    prom=acum/cont
    print("El promedio de puntos es de =",prom)

def classe(b):
    for x in lista:
        if num_puntos == 0 and num_puntos <= 40:
            clasificacion = "Amateur"
        elif num_puntos >= 41 and num_puntos <= 80:
            clasificacion = "Principiante"
        elif num_puntos >= 81 and num_puntos <= 120:
            clasificacion = "Avanzado"
        elif num_puntos >= 120:
            clasificacion = "idolo"


while True:
    try:
        print("********** Torneo Nacional de Basket 2024 ***********")
        print("1-. Agregar Equipo")
        print("2-. Lista equipos")
        print("3-. Actualizar lista de equipos por id")
        print("4-. Generar BBDD")
        print("5-. Cargar BBDD")
        print("6-. Estadisticas")
        print("0-. Salir")

        op = int(input("Ingrese operacion a realizar: \n"))

        if op == 1:
            print("")
            print("********** Agregar Equipo **********")
            print("")
            id_equipo = int(input("Ingrese ID: \n"))
            nombre = input("Ingrese Nombre de quipo: \n")
            num_puntos = int(input("Ingrese Cantidad de puntos: \n"))
            ''''''
            if num_puntos ==0 and num_puntos <=40:
                clasificacion = "Amateur"
            elif num_puntos >=41 and num_puntos <=80:
                clasificacion = "Principiante"
            elif num_puntos >=81 and num_puntos <=120:
                clasificacion = "Avanzado"
            elif num_puntos >=120:
                clasificacion = "idolo"
            ''''''
            listadatos = [id_equipo,nombre,num_puntos,clasificacion]
            lista.append(listadatos)
            print ("Datos cargados correctamente...")

        elif op == 2:
            print("")
            print("********** Lista de equipos **********")
            print("")
            for x in lista:
                print("ID: ", x[0],"Nombre de equipo: ",x[1],"Numero de puntos: ",x[2],"Clasificacion: ",x[3])

        elif op == 3:
            print("")
            print("********** Actualizar nombre de equipo **********")
            print("")
            id_buscar=int(input("Ingrese ID de equipo: \n"))
            cambio_nombre(id_buscar)


        elif op == 4:
            print ("")
            print ("*********** Generando CSV **********")
            print ("")
            with open('bbdd_equipos.csv','w',newline='') as bbdd_equipos:
                escritor_csv = csv.writer(bbdd_equipos)
                escritor_csv.writerow(['id','nombre','puntos','clasificacion'])
                escritor_csv.writerow(lista)
                print("")
                print("Archivo generado correctamente.... ")
        elif op == 5:
            print("")
            print("*********** Cargar CSV **********")
            print("")
            with open ('bbdd_equipos.csv','r',newline='') as bbdd_equipos:
                lector_csv=csv.reader(bbdd_equipos)
                for x in lector_csv:
                    lista.append(x)
                print("Csv Cargado exitosamente")
        elif op == 6:
            print("")
            print("********** Estadisticas **********")
            print("")
            estadisticas()


        elif op == 0:
            print("Adios")
            break
    except:
        print("Se ha producido un error")
