DOMINIO = [(-5, 5), (-5, 5)]
INCREMENTO = 0.1

xContinuidad = DOMINIO[0][0]
yContinuidad = DOMINIO[1][0]
xMax = float("{:.2f}".format(DOMINIO[0][1]))
yMax = float("{:.2f}".format(DOMINIO[1][1]))
puntosDiscontinuidad = []

def cambiarPunto():
    global xContinuidad, yContinuidad, xMax, INCREMENTO
    xContinuidad += INCREMENTO
    xContinuidad = float("{:.2f}".format(xContinuidad))
    if xContinuidad == xMax:
        xContinuidad = DOMINIO[0][0]
        yContinuidad += INCREMENTO
        yContinuidad = float("{:.2f}".format(yContinuidad))

def estudioContinuidad(funcion):
    global yContinuidad
    while yContinuidad <= yMax:
        try:
            funcion(xContinuidad, yContinuidad)
            cambiarPunto()
            
        except:
            # Si los valores son enteros los guardamos como tal
            if (xContinuidad % 2 == 0 and yContinuidad % 2 == 0):
                xDiscontinua = int(xContinuidad)
                yDiscontinua = int(yContinuidad)
            else:
                xDiscontinua = xContinuidad
                yDiscontinua = yContinuidad

            puntosDiscontinuidad.append((xDiscontinua, yDiscontinua))
            cambiarPunto()
    
    return puntosDiscontinuidad