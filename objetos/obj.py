def aumentar_speed(botas : int, speed : int)->int:
    vel_aumentada = speed + botas
    return vel_aumentada

def aumentar_damage(espada : int, damage : int)->int:
    dam_aumentado = damage + espada
    return dam_aumentado 

def lista_objetos():
    return ("1. Botas (Grebas de berserker)\n"
            "2. Espada (Baile de la muerte)")