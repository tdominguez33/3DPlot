# Librerias utilizadas
import numpy as np
import matplotlib.pyplot as plt
from continuidad import estudioContinuidad

# Definimos el dominio en el que vamos a evaluar la función: [Dom(X), Dom(Y)]
DOMINIO = [(-5, 5), (-5, 5)]

# Establecemos la función
def funcion(x, y):
    return (x**2)*(np.cos(y/2) + np.sin(y/3))**2

# Función que genera los gráficos
def plot_superficie(dominio, funcion, grid_samples=50, **plot_kwargs):
    x = np.linspace(dominio[0][0], dominio[0][1], grid_samples)
    y = np.linspace(dominio[1][0], dominio[1][1], grid_samples)
    
    X, Y = np.meshgrid(x, y)
    fn_vectorized = np.vectorize(funcion)
    Z = fn_vectorized(X, Y)

    # Tamaño de la ventana
    fig = plt.figure(figsize=(15, 8))

    # Figura 3D
    ax = fig.add_subplot(1, 2, 1, projection = "3d")
    surf = ax.plot_surface(X, Y, Z, **plot_kwargs)
    ax.set(xlabel="X", ylabel="Y", zlabel="f(x, y)", title="Superficie")
    fig.colorbar(surf, shrink=0.5, aspect=8)
    
    # Curvas de Nivel
    ax = fig.add_subplot(2, 2, 2)
    ax.set(xlabel = "X", ylabel = "Y", title = "Curvas de Nivel")
    ax = plt.contour(X, Y, Z, levels = 8, **plot_kwargs)
    ax.clabel(fontsize = 8)

    # Estudio de Continuidad
    ax = fig.add_subplot(2, 2, 4)
    ax.set(xticks = [], yticks = [], xticklabels = [], yticklabels = [])
    
    # Si hay al menos un punto de discontinuidad
    if estudioContinuidad(funcion) != []:
        ax.text(0.3, 0.5, "La función es Discontinua en: \n" + str(estudioContinuidad(funcion)))
    else:
        # Si no hay puntos de discontinuidad
        ax.text(0.25, 0.5, "La función no presenta discontinuidad")
    
    # Mostramos todo
    plt.show()

    return fig, ax

# Gráficamos la función con nuestros valores
fig, ax = plot_superficie(DOMINIO, funcion, cmap='gist_ncar')
