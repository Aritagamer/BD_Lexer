import os
import time
import Conexion_SQL as SQL

#_____________________________________________________SUBMENU SALAS_____________________________________________________________
Ins = ['BIG ERROR','1er Almacen','2do Almacen','Enfermeria','Comedor','Quirofano','Urgencias']

def Mostr_sala (tipo = 0):
    os.system("cls")

    find = SQL.consulta_BD(
        """
            SELECT * FROM SALAS WHERE ID = '%s'
        """,
        (tipo)
    )

    
    print("%-25s %2s %25s %25s %-2s" %("Nombre","ID","Ubicacion","Responsable","Horario",))
    
    for i in find:
        print("%-25s %2s %25s %25s %-2s" %i)
    input()


def Mod_sala (tipo = 0):
    os.system("cls")
    
    print("Ingrese los nuevos datos de la sala.\n\n")

    print("Ubicacion:",end = " ")
    Ubi = input()
    print("Responsable:",end = " ")
    Resp = input()
    print("Horario:",end = " ")
    Hor = input()

    try:
        SQL.Actualizar_BD(
            """
                UPDATE SALAS SET
                UBICACION = '%s',
                RESPONSABLE  = '%s',
                HORARIO = '%s'
                WHERE ID = '%s'
            """,
            (Ubi,Resp,Hor,tipo)
        )
    except Exception as e:
        print("Ocurrio el error: ",e)

        time.sleep(5)
        return

    print("\n\nSala actualizado con exito")
    time.sleep(1)

    return