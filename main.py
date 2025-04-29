"""En el main estan importadas todas las funciones y los atributos
nececsarios para la ejecucion de las condiciones solicitadas
"""

from objetos.obj import lista_objetos
from utilidades.estadisticas import equipar_objeto
from utilidades.menu import mostrar_menu, leer_opcion
from campeones.camp import lista_campeones, mostrar_atributos, habilidad_definitiva
from campeones.camille import cam_damage, cam_health, cam_b_speed, cam_definitiva, camille_name
from campeones.lux import lux_damage, lux_health, lux_b_speed, lux_definitiva, lux_name
from campeones.thresh import thresh_damage, thresh_health, thresh_b_speed,thresh_definitiva, thresh_name

print("Bienvenidos a la grieta del invocador")
print("--------------------------")

print(mostrar_menu(),"\n")
#Mostramos el menu desde una funcion como se solicito

opcion = leer_opcion("Elija una opcion: ", 1 , 4)
#Tenemos la funcion leer_opcion para validar las opciones

print("--------------------------")

"""Anidamos condicionales, adentro de match y case, y volvemos
a usar match y case dentro de esos condicionales para invocar
a las funciones correspondientes a cada eleccion del usuario
"""

match opcion:
    case 1:
        
        """primer case
        una vez seleccionada la opcion mostrar atributos
        pedimos al usuario que elija el campeon, cuyos
        atributos desee ver
        """
        
        print(lista_campeones())
        campeon_elegido = leer_opcion("Elija un campeón: ", 1,3)
        print("--------------------------")
        if campeon_elegido == 1:
            print(camille_name+"\n"+mostrar_atributos(cam_damage, cam_health, cam_b_speed))
        elif campeon_elegido == 2:
            print(lux_name+"\n"+mostrar_atributos(lux_damage, lux_health, lux_b_speed))
        else:
            print(thresh_name+"\n"+mostrar_atributos(thresh_damage, thresh_health, thresh_b_speed))
    case 2:
        
        """El segundo case es similar, solo que
        solicitamos que elija el campeon, cuya Habildiad
        definitiva(Ulti) desea utilizar
        """
        
        print(lista_campeones())
        campeon_elegido = leer_opcion("Elija un campeón: ", 1,3)
        print("--------------------------")
        if campeon_elegido == 1:
            print(camille_name+"\n"+habilidad_definitiva(cam_definitiva))
        elif campeon_elegido == 2:
            print(lux_name+"\n"+habilidad_definitiva(lux_definitiva))
        else:
            print(thresh_name+"\n"+habilidad_definitiva(thresh_definitiva))
    case 3:
        
        """Ya en el tercer case, una vez ingresado
        a la opcion equipar objeto. Solicitamos:
        1ro Que elija el campeon
        2do Que elija el objeto
        y con match, segun el objeto y campeon
        elejido, invocamos a la funcion con el
        parametro que le corresponda
        """
        
        print(lista_campeones())
        campeon_elegido = leer_opcion("Elija un campeón: ", 1, 3)
        print("--------------------------")
        if campeon_elegido == 1:
            print(lista_objetos())
            objeto_elegido = leer_opcion("Elija un objeto: ", 1, 2)
            print("--------------------------")
            match objeto_elegido:
                case 1:
                    print(equipar_objeto(objeto_elegido, cam_b_speed))
                case 2:
                    print(equipar_objeto(objeto_elegido, cam_damage))
        elif campeon_elegido == 2:
            print(lista_objetos())
            objeto_elegido = leer_opcion("Elija un objeto: ", 1, 2)
            print("--------------------------")
            match objeto_elegido:
                case 1:
                    print(equipar_objeto(objeto_elegido, lux_b_speed))
                case 2:
                    print(equipar_objeto(objeto_elegido, lux_damage))
        else:
            print(lista_objetos())
            objeto_elegido = leer_opcion("Elija un objeto: ", 1, 2)
            print("--------------------------")
            match objeto_elegido:
                case 1:
                    print(equipar_objeto(objeto_elegido, thresh_b_speed))
                case 2:
                    print(equipar_objeto(objeto_elegido, thresh_damage))
    case 4:
        #sigo usando exit para salir por no se como hacerlo de otra manera
        exit()


