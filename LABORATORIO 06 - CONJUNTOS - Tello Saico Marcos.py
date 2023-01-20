
##LABORATORIO 06 - CONJUNTOS - Tello Saico Marcos

## - Realizar operaciones de unión, intersección y diferencia de conjuntos
conjunto1_frutas={"plátano","pera","manzana","tomate"}
conjunto2_verduras={"apio","zapallo","papa","tomate"}
conjunto3_plantas={"lechuga","espinaca","espárragos","tomate"}

print("Union")

union_conjuntos = conjunto1_frutas.union(conjunto2_verduras,conjunto3_plantas)

print("Contenido de la variable union_conjuntos: ", union_conjuntos)
print("Cantidad de elementos de la variale union_conjuntos: ", len(union_conjuntos))
print("Tipo de dato de la variable union_conjuntos : ", type(union_conjuntos))
print()
print("Intersección")

interseccion_conjuntos = conjunto1_frutas.intersection(conjunto2_verduras,conjunto3_plantas)

print("Contenido de la variable interseccion_conjuntos: ", interseccion_conjuntos)
print("Cantidad de elementos de la variale interseccion_conjuntos: ", len(interseccion_conjuntos))
print("Tipo de dato de la variable interseccion_conjuntos : ", type(interseccion_conjuntos))
print()

## - Calcular la diferencia entre dos conjuntos
print("diferencia")

diferencia_conjuntos = conjunto1_frutas.difference(conjunto2_verduras,conjunto3_plantas)

print("Contenido de la variable diferencia_conjuntos: ", diferencia_conjuntos)
print("Cantidad de elementos de la variale diferencia_conjuntos: ", len(diferencia_conjuntos))
print("Tipo de dato de la variable diferencia_conjuntos : ", type(diferencia_conjuntos))
print()
## - Calcular la diferencia simétrica entre 3 conjuntos
print("diferencia simétrica")

diferencia_simetrica_conjuntos1 = conjunto1_frutas.symmetric_difference(conjunto2_verduras)
diferencia_simetrica_conjuntos2 = conjunto2_verduras.symmetric_difference(conjunto3_plantas)

print("Contenido de la variable diferencia_simetrica_conjuntos1: ", diferencia_simetrica_conjuntos1)
print("Contenido de la variable diferencia_simetrica_conjuntos2: ", diferencia_simetrica_conjuntos2)
