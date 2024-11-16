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

def Minimos_Cuadrados(x_data, y_data, x_vals):
    polinomio = np.polynomial.Polynomial.fit(x_data, y_data, 5)
    plt.plot(x_data, y_data, 'o', label='Datos')
    plt.plot(x_vals, polinomio(x_vals), label='Polinomio Ajustado')
    plt.title('Polinomio de Mínimos Cuadrados')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()
    return polinomio(x_vals)