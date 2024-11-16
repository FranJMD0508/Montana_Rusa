import numpy as np
from pandas import read_csv
import unittest
from src.metodos import Minimos_Cuadrados

class TestCubico(unittest.TestCase):
    def test_minimos_cuadrados(self): 
        datos = read_csv('minimos_cuadrados.csv')
        x_data = datos['x'].values
        y_data = datos['y'].values
        valores = datos["x_vals"].values
        x_vals = np.linspace(valores[0], valores[1], int(valores[2]))
        resultado = Minimos_Cuadrados(x_data, y_data, x_vals)
        np.testing.assert_allclose(resultado[0], 1.1, atol=0.1)

unittest.main()