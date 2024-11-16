import numpy as np
from pandas import read_csv
import unittest
from src.metodos import Sistema_Ecuaciones

class TestCubico(unittest.TestCase):
    def test_poligono_ortogonal(self): 
        datos = read_csv('src/sistema_ecuaciones.csv')
        a = np.array(datos.iloc[:, :-1].values)
        b = np.array(datos.iloc[:, -1].values)
        resultado = Sistema_Ecuaciones(a,b)
        np.testing.assert_allclose(resultado, np.linalg.solve(a,b), atol=0.1)

unittest.main(argv=['first-arg-is-ignored'], exit=False)