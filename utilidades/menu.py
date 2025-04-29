def mostrar_menu():
    
    """no recibimos parametros
    simplemente devuelve el
    menu en string"""
    
    return ("1. Mostrar atributos del campeón\n"
            "2. Usar habilidad definitiva\n"
            "3. Equipar objeto y mostrar estadísticas\n"
            "4. Salir"   
            )
    

def leer_opcion(prompt : str, minimo: int, maximo : int)-> int:
    
    """Definimos como parametro un mensaje(prompt)
    , un maximo y un minimo.
    Esto nos permite reutilizar la funcion 
    para validar distintas cantidad de opciones
    y con distintos mensajes (prompt)
    """
    
    while True:
        opcion = input(prompt)
        
        """Una vez que el usuario ingresa una opcion
        validamos con la funcion isdigit, que no haya 
        caracter alfabetico y sea 1 digito.
        Si NO cumple esa condicion, imprime un mensaje y vuelve
        a entrar al bucle.
        Si cumple la condicion del if, que sea una opcion
        entre el minimo y maximo definido por parametro,
        retorna la opcion y rompe el bucle
        """
        
        if opcion.isdigit():
            
            #una vez que se valida el digido, casteamos a int
            
            opcion = int(opcion)
            
            #necesitamos castear para comprar la condicion
            #si no casteamos, estamos comparando un str con un int
            
            if minimo <= opcion <= maximo:
                return opcion
            else:
                print(f"Ingrese un numero entre {minimo} y {maximo}")
        else:
            print(f"Ingrese un numero entre {minimo} y {maximo}")
            

        

    
    
