def mostrar_atributos(damage  : int,health : int,speed : int)->str:
    
    """llamamos en el main y toma de parametro
    las variables declaradas en los campeones
    Returns:
        str: devolvemos los atributos
    """
    
    atributos = (f"Damage:{damage}\nHealth:{health}\nBase Speed:{speed}")
    return atributos

def habilidad_definitiva(definitiva : str)->str:
    
    """llamamos en el main, y el parametro
    esta definido en el campeon que use la habilidad
    Returns:
        str: devolvemos el detalle de la definitiva
    """
    
    ulti =  definitiva
    return  ulti

def lista_campeones():
    
    """Definimos una funcion
    para mostrar el menu de campeones
    que vamos a reutilizar mas de una vez
    """
    
    return ("1. Camille\n"
        "2. Lux\n"
        "3. Thresh")
