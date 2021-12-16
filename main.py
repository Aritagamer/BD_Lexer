import os
import time

import Pascientes as mn1
import Personal as mn2
import Insumos as mn3
import Salas as mn4

def mk_menu(titulo = "", elem = [],funci = []):


    r = -1
    while r != len (elem):
        r = -1
        while r < 1 or r > len (elem) + 1 :

            os.system("cls")
            print( "%s" %(titulo), end="\n\n" )
            for i, el in enumerate(elem, start=1):

                
                print("%2d" %(i),end="")

                print("\t%s" %(el))

            r = int (input())
        
        for i, fu in enumerate(funci,start = 1):

            if i == r:
                    
                    fu()
                    #print (r)
        if r == len (elem):
            #print("Conasupo")
            return
        
                     

    return




  



        
    




if __name__ == "__main__":
    os.system("mode con cols=200 lines=50")
    os.system("cls")

    print("Bienvenido al sistema de Gestion del Hospital")
    time.sleep(1)
    
    

    mk_menu(
    titulo = "Elija la opcion que desea visualizar",
    elem = ["Pacientes","Personal", "Insumos","Salas", "Salir"],
    funci = [
        lambda:mk_menu
        (
            titulo="MENU: 'Pacientes' ",
            elem = ["Lista de pacientes","Citas","Regresar al menu anterior"],
            funci = [
                lambda:mk_menu
                (
                titulo = "Menu: 'Lista de pacientes'",
                elem = ["Mostrar pacientes","Dar de alta paciente","Modificar paciente","Eliminar paciente","Regresar al menu anterior"],
                funci = [lambda:mn1.Mostr_Pac() ,lambda:mn1.Alta_Pac(), lambda:mn1.Modif_Pac(), lambda:mn1.Elim_Pac()]
                ),
                lambda:mk_menu
                (
                titulo = "Menu: 'Citas'",
                elem = ["Mostrar Citas","Generar nueva cita","Modificar cita","Eliminar cita","Regresar al menu anterior"],
                funci = [lambda:mn1.Mos_cita() ,lambda:mn1.Gen_cita(), lambda:mn1.Mod_cita(), lambda:mn1.Elim_cita()]
                ),
                ] 
        ),
        lambda:mk_menu(
            titulo="MENU: 'Personal' ",
            elem = ["Lista de personal","Horario de personal","Dar de alta personal","Modificar personal","Eliminar personal","Regresar al menu anterior"],
            funci = [lambda:mn2.Mostr_Per(), lambda:mn2.Hor_Per() ,lambda:mn2.Alta_Per() ,lambda:mn2.Modif_Per(), lambda:mn2.Elim_Per()] ),
        lambda:mk_menu(
            titulo="MENU: 'Insumos' ",
            elem = ["Medicamentos","Instrumentos","Aparatos","Material","Regresar al menu anterior"],
            funci = [] ),
        lambda:mk_menu(
            titulo="MENU: 'Salas' ",
            elem = ["1er Almacen","2do Almacen","Enfermeria","Comedor","Quirofano","Urgencias","Regresar al menu anterior"],
            funci = [] )
    ])
            

    

  