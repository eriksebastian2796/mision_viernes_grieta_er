"""
Importamos las variables, y las funciones del paquete
objetos, que vamos a necesitar en este modulo
"""

from objetos.botas import grebas_de_berserker
from objetos.espada import baile_dela_muerte
from objetos.obj import aumentar_damage
from objetos.obj import aumentar_speed

def equipar_objeto(objeto : int, atributo : int)->int:
    
    """
    Definimos el parametro objeto, que va a ser
    la selecion que hagamos en el menu, y el
    parametro atributo(es la variable definida en el
    campeon a equipar)
    En cada opcion , tenemos un objeto, que aumenta
    al atributo correspondiente
    """
    
    match objeto:
        case 1:
                velocidad_aumentada = aumentar_speed(grebas_de_berserker, atributo)
                return f"Objeto equipado, speed aumentada:{atributo} >>> {velocidad_aumentada}"
        case 2:
                damage_aumentado = aumentar_damage(baile_dela_muerte,  atributo)
                return f"Espada equipada, damage aumentado:{atributo} >>> {damage_aumentado}"
           