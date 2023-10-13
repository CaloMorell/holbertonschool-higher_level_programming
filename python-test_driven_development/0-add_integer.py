#!/usr/bin/python3
"""Este módulo contiene una función que devuelve
     la suma de dos números enteros.
"""


def add_integer(a, b=98):
    """Suma dos números enteros.

     Argumentos:
         a (int): el primer argumento debe ser un número entero o flotante.
         b (int): el segundo argumento debe ser un número entero o flotante.
                     valor predeterminado: 98
     Sube:
         TypeError: var debe ser un número entero.
         TypeError: var debe ser un número entero.

     Devoluciones:
         int: devuelve la suma de a y b.
     """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
