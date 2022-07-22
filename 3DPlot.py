import numpy as np
import matplotlib.pyplot as plt

mapaColor = 'gist_ncar'

def plot_superficie(dominio, funcion, grid_samples=50, **plot_kwargs):
    x = np.linspace(dominio[0][0], dominio[0][1], grid_samples)
    y = np.linspace(dominio[1][0], dominio[1][1], grid_samples)
    
    X, Y = np.meshgrid(x, y)
    
    fn_vectorized = np.vectorize(funcion)
    Z = fn_vectorized(X, Y)
    
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(1, 2, 1, projection = "3d")
    surf = ax.plot_surface(X, Y, Z, **plot_kwargs)
    ax.set(xlabel="X", ylabel="Y", zlabel="f(x, y)", title="Superficie")
    fig.colorbar(surf, shrink=0.5, aspect=8)
    ax = fig.add_subplot(1, 2, 2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    ax.set_title('Curvas de Nivel')
    ax = plt.contour(X, Y, Z, levels = 20, **plot_kwargs)
    
    plt.show()

    return fig, ax


def funcion(x, y):
    return (x**2)*(np.cos(y/2) + np.sin(y/3))**2
    
dominio = [(-5, 5), (-5, 5)] 
fig, ax = plot_superficie(dominio, funcion, cmap=mapaColor)
