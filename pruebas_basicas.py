#CREAR UNA FUNCION return Y UTILIZARLA

def sumar_ints(a,b):
    """"SUMA DOS NUMEROS ENTEROS"""
    if type(a) == int and type(b) == int:
        return a + b
    else:
        print("A O B NO SON TIPO INT, NO SE PUEDEN SUMAR")


a = 10
b = 20
c = sumar_ints(a,b)
print(c)
print("\n----------------------------------------------------------")

#Debemos de tener en cuneta el orden de los parametros posicionales, a no ser que usemos argumentos clave-valor,
#Para el cual no importaría el orden en el que se añaden los argumentos a la función que vayamos a usar.

def mostar_valores(a,b):
    """"NOS MUESTRA QUE EL VALOR A ES ALEXANDRA Y QUE EL VALOR B ES FLORIN, PARA COMPROBAR QUE ES IMPORTANTE
        EL USO DE LOS PARAMETROS POSICIONALES"""
    print("El primer valor que hemos introducido es: ",a,"como podemos obeservar, se trata de Alexandra")
    print("El primer valor que hemos introducido es: ",b,"como podemos obeservar, se trata de Florin")
    
mostar_valores("Alexandra","Florin")
print("\n----------------------------------------------------------")
mostar_valores("Florin","Alexandra") ##CON ESTE PODEMOS OBSERVAR LA IMPOTANCIA DEL ORDEN DE LOS ARGUMENTOS QUE PASAMOS
                                     # A LAS FUNCIONES
print("\n----------------------------------------------------------")

c = sumar_ints(a=20,b=30) ##UTILIZAMOS CLAVE-VALOR, ES DECIR, ASOCIAMOS EL VALOR YA A LOS PARAMETROS
print(c)
print("\n----------------------------------------------------------")



##USO DE PARAMETROS PREDETERMINADOS, POR SI NO SE PASAN TODOS LOS ARGUMENTOS A LA FUNCION, QUE SE RECONOZCA
# ES IMPORANTE SABER, QUE LOS VALORES PREDETERMIANDOR Y LOS ARGUMENTOS CLAVE-VALOR VAN DESPUÉS DE LOS ARGUMENTOS
# POSICIONALES

def comprobar_ambos_par(a,b=2):
    if (type(a) == int or type(a) == float) and type(b) == int or type(b) == float:
        if a % 2 == 0: print("El numero",a,"es de tipo:",type(a),"y es un numero par")
        else: print("El numero",a,"es de tipo:",type(a),"y no es un numero par")

        if b % 2 == 0: print("El numero",b,"es de tipo:",type(b),"y es un numero par")
        else: print("El numero",b,"es de tipo:",type(b),"y no es un numero par")


comprobar_ambos_par(10) ##USAMOS SOLO EL PARAMETRO a, el otro tiene valor predeterminado de 2
print("\n----------------------------------------------------------")
comprobar_ambos_par(12.0,5)
print("\n----------------------------------------------------------")
comprobar_ambos_par(3)
print("\n----------------------------------------------------------")

