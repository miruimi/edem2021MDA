nombre: str =input("Nombre de la pelicula: ")
año: int=input("Año de la pelicula: ")

puntuacion:float = 0
while (puntuacion<1 or puntuacion>5):
    puntuacion = float(input("Puntuacion de la pelicula: "))
    if(puntuacion <1 or puntuacion> 5):
        print ("Valor fuera de rango")

director: str = input("Nombre de director: ")
genero =['comedia','drama', 'terror', 'acción']

generoelegido:bool = False
tipogenero: None
while (not generoelegido):
     tipogenero= input("Genero de la pelicula: ")
     if(tipogenero not in genero):
         print ("Eso no es un tipo de genero")
     else: generoelegido = True

Pelicula = {"nombre: ": nombre, "año: " : año, "puntuacion: ": puntuacion, "director: ": director,"genero: ": tipogenero}

print ("Critica realizada")