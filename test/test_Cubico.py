import numpy as np
from pandas import read_csv
import unittest, sys, os

from src.metodos import Trazador_Cubico 
class TestCubico(unittest.TestCase):
    def test_trazador_cubico(self):
        datos = read_csv('src/trazado_cubico.csv')
        x_data = datos['x'].values
        y_data = datos['y'].values
        valores = datos["x_vals"].values
        x_vals = np.linspace(valores[0], valores[1], int(valores[2]))
        resultado = Trazador_Cubico(x_data, y_data, x_vals)
        np.testing.assert_allclose(resultado[0], 0.5, atol=0.1)

unittest.main(argv=['first-arg-is-ignored'], exit=False)