import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def Trazador_Cubico(x_data, y_data, x_vals):
    trazado = sp.interpolate.CubicSpline(x_data, y_data)
    plt.plot(x_data, y_data, 'o', label='Datos')
    plt.plot(x_vals, trazado(x_vals), label='Trazador Cúbico')
    plt.title('Método de Trazador Cúbico Sujeto')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()
    return trazado(x_vals)