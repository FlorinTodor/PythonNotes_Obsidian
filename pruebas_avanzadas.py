###VAMOS A CREAR FUNCIONES QUE LE PODAMOS PASAR UN NUMERO ARBITRARIO DE ARGUMENTOS, UN NUMERO ARBITRARIO DE ARGUMENTOS
### CLAVE-VALOR, USO DE TODOS LOS TIPOS DE PASO DE PARAMETROS Y EL USO DE LA IMPORTACION DE FUNCIONES

def muestra_lista(nombre,apellido,*args):
    """"MUESTRA POR PANTALLA EL NOMBRE Y APELLIDO, Y EL RESTO DE ARGUMENTOS SI SE LES PASA"""
    print("El nombre de la persona es:",nombre.title())
    print("Los apellidos de la persona son:",apellido.title())
    print("\nVamos a mostrar el resto de parametros asociados a la persona:\n")

    if type(args) == dict:
        mostrar_informacion_diccionario(args)
    else:    
        for arg in args: ##NO SABEMOS QUE SE HA PASADO, SI ES DINERO O EL QUE
            print(arg)

muestra_lista("florin emanuel","todor gliga","150000€","soltero","estudiante","con ganas de aprender")        

##podemos hacer un return en esa funcion y devolver los argumentos, que se han pasado en arg, como una tupla

def muestra_lista_2(nombre,apellido,*args):
    """"MUESTRA POR PANTALLA EL NOMBRE Y APELLIDO, Y DEVUEL EL RESTO DE ARGUMENTOS QUE SE LES PASA"""
    print("El nombre de la persona es:",nombre.title())
    print("Los apellidos de la persona son:",apellido.title())
    
    return args


print("\n----------------------------------------------------------------------------------------------------------")

argumentos = muestra_lista_2("florin emanuel","todor gliga","150000€","soltero","estudiante","con ganas de aprender")   

for argumento in argumentos:
    print(argumento)


print("\n----------------------------------------------------------------------------------------------------------")    



##PODEMOS PASARLE ARGUMENTOS ARBITRARIOS DE CLAVE-VALOR
def mostrar_informacion_lista(lista):
    for objeto in lista:
        print(objeto)

def mostrar_informacion_diccionario(diccionario):
    if type(diccionario) == dict:
        for key, value in diccionario.items():
            print(key, value)

def muestra_diccionario(nombre, apellidos, **kwargs):
    print("El nombre de la persona es:", nombre.title())
    print("Los apellidos de la persona son:", apellidos.title())

    for key, values in kwargs.items():
        if isinstance(values, (list, tuple)):
            print("La clave es:", key)
            print("Los valores son:")
            mostrar_informacion_lista(values)
        elif isinstance(values, dict):
            print("La clave es:", key)
            print("Los valores son:")
            mostrar_informacion_diccionario(values)
        else:
            print(key,values)


def muestra_diccionario_2(nombre, apellidos, **kwargs):
    print("El nombre de la persona es:", nombre.title())
    print("Los apellidos de la persona son:", apellidos.title())

    return kwargs ##Nos devuelve un diccionario con todos los clave-valor




muestra_diccionario("florin emanuel", "todor gliga", dinero="150000€", estado_civil="soltero", estado_Actual="estudiante")


print("\n----------------------------------------------------------------------------------------------------------")    


diccionario = muestra_diccionario_2("florin emanuel", "todor gliga", dinero="150000€", estado_civil="soltero", estado_Actual="estudiante")

print(diccionario)

print("\n----------------------------------------------------------------------------------------------------------")    

mostrar_informacion_diccionario(diccionario)
