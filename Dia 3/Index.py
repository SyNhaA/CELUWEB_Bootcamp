mi_texto =  "Esta es una prueba"
resultado = mi_texto[0]
#Letra a buscar, desde el indice que empieza hasta el indice final
resultado2 = mi_texto.index("a",5,10)
#busca de derecha a izquierda
resultado2 = mi_texto.rindex("a")

print(resultado2)