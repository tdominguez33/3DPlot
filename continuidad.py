DOMINIO = [(-5, 5), (-5, 5)]

# De a cuanto vamos aumentando los valores de X e Y para recorrer la función (Cambiar dependiendo la función)
INCREMENTO = 0.1

# Variables que vamos a ir cambiando a medida que recorremos
xContinuidad = DOMINIO[0][0]
yContinuidad = DOMINIO[1][0]

# Variable donde se guardan los puntos de discontinuidad que vayamos encontrando
puntosDiscontinuidad = []

# Valores máximos, los guardamos como floats de dos decimales
xMax = float("{:.2f}".format(DOMINIO[0][1]))
yMax = float("{:.2f}".format(DOMINIO[1][1]))

# Función que se encarga de cambiar los puntos en los que estamos
def cambiarPunto():
    global xContinuidad, yContinuidad, xMax, INCREMENTO
    xContinuidad += INCREMENTO
    xContinuidad = float("{:.2f}".format(xContinuidad))

    # Si llegamos al punto máximo volvemos al mínimo y cambiamos el valor de Y
    if xContinuidad == xMax:
        xContinuidad = DOMINIO[0][0]
        yContinuidad += INCREMENTO
        yContinuidad = float("{:.2f}".format(yContinuidad))

# Función que realiza el estudio de continuidad y devuelve los puntos en los que la función no está definida
def estudioContinuidad(funcion):
    global yContinuidad

    # Mientras no nos pasemos del valor máximo de Y
    while yContinuidad <= yMax:

        # Intentamos definir la función en ese punto especifico
        try:
            funcion(xContinuidad, yContinuidad)
            cambiarPunto()
        
        # Si la definición de la función da error guardamos el punto
        except:
            # Si los valores son enteros los guardamos como tal, sino guardamos como están
            if (xContinuidad % 2 == 0 and yContinuidad % 2 == 0):
                xDiscontinua = int(xContinuidad)
                yDiscontinua = int(yContinuidad)
            else:
                xDiscontinua = xContinuidad
                yDiscontinua = yContinuidad

            puntosDiscontinuidad.append((xDiscontinua, yDiscontinua))
            cambiarPunto()
    
    return puntosDiscontinuidad