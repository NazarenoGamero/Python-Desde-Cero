"""
Programa para saber si la letra es vocal o no lo es.
"""

import gettext 


vocales = {'a','e','i','o','u'}

def isvocal(letra):
    """
Funcion para saber si la letra es vocal o no, primero corrobora que sea una letra, y que sea un solo caracter
    """
    if len(letra) == 1:
        if letra.isalpha(): 
            if letra in vocales:
                return True
            else:
                return False
        else:
            return "No es una letra."
    else: 
        return "Es mas de un caracter."

letra = input("Inserte la letra que quiere corroborar si es vocal o no: ")
print("\n",isvocal(letra))