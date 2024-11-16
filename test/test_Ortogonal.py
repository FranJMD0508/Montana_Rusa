import numpy as np
from pandas import read_csv
import unittest
from src.metodos import Polinomio_Ortogonal

class TestCubico(unittest.TestCase):
    def test_polinomio_ortogonal(self):
        datos = read_csv('src/polinomio_ortogonal.csv')
        x_data = datos['x'].values
        y_data = datos['y'].values
        valores = datos["x_vals"].values
        x_vals = np.linspace(valores[0], valores[1], int(valores[2]))
        resultado = Polinomio_Ortogonal(x_data, y_data, x_vals)
        np.testing.assert_allclose(resultado[0], 1.1, atol=0.1)

unittest.main(argv=['first-arg-is-ignored'], exit=False)