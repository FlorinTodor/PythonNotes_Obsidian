import pruebas_avanzadas as p ##Hemos aprendido a como importar modulos

lista = ["coche","moto","avion"]

p.muestra_lista("florin emanuel","todor gliga",lista)

##HAY QUE SABER LA DIFERENCIA ENTRE UNA LISTA Y UN DICCIONARIO PARA EL USO DE *ARGS Y DE **KWARGS

diccionario = {
    "coche":"bmw",
    "años" : 5,
    "matricula": "435FR43"
    }

print("\n---------------------------------------------------------------------------------\n")
p.muestra_lista("florin emnauel","todor gliga",diccionario)

