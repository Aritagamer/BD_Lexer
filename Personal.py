import os
import time
import Conexion_SQL as SQL


#_____________________________________________________SUBMENU PERSONAL_____________________________________________________________

def Alta_Per():
    os.system("cls")
    print("Se procedera a dar de alta a un nuevo personal espere")
    time.sleep(1)
    os.system("cls")
    print("Porfavor Proporcione los datos que se le piden acontinuacion:",end = "\n\n")
    
    print("Numero de Empleado:",end = " ")
    NE = input()
    
    find = SQL.consulta_BD(
        """
            SELECT * FROM PERSONAL WHERE NUM_EMPL = '%s'
        """,
        (NE)
    )
    if find:
        os.system("cls")
        print("Personal registrado con anterioridad revise el numero de empleado")
        time.sleep(1)

        return
    
    print("Nombre (Apellido Paterno, Materno, Nombre):",end = " ")
    name = input()
    print("Horario:",end = " ")
    Hor = (input()).upper()
    print("Fecha de ingreso (DD/MM/AA):",end = " ")
    Ing = input()
    print("Especialidad:",end = " ")
    Esp = input()
    

    try:
        SQL.Actualizar_BD(
            """
                INSERT INTO PERSONAL 
                VALUES ('%s' , '%s', '%s', '%s', '%s')
            """,
            (name,NE,Hor,Ing,Esp)
        )
    except Exception as e:
        print("Ocurrio el error: ",e)

        time.sleep(5)
        return

    print("\n\nPersonal dado de alta con exito")
    time.sleep(1)

    return

def Mostr_Per ():
    os.system("cls")

    find = SQL.consulta_BD(
        """
            SELECT * FROM PERSONAL
        """,
        ()
    )
    if not find:
        print ("Nada que mostrar aun")
        time.sleep(1.5)
        return
    
    print("%-25s %8s %2s %10s %-30s" %("Nombre","Num. Emp","Hor","Ingreso","Especialidad",))
    
    for i in find:
        print("%-25s %8s %2s %10s %-30s" %i)
    input()

def Modif_Per ():
    os.system("cls")
    print("Escriba el numero de empleado que desea modificar:", end = " ")
    NE = input()
    
    find = SQL.consulta_BD(
        """
            SELECT * FROM PERSONAL WHERE NUM_EMPL = '%s'
        """,
        (NE)
    )
    if not find:
        os.system("cls")
        print("El personal no esta registrado revise el numero de empleado")
        time.sleep(1)

        return
    os.system("cls")
    
    print("Ingrese los nuevos datos del personal.\n\n")

    print("Nombre (Apellido Paterno, Materno, Nombre):",end = " ")
    name = input()
    print("Horario:",end = " ")
    Hor = (input()).upper()
    print("Fecha de ingreso (DD/MM/AA):",end = " ")
    Ing = input()
    print("Especialidad:",end = " ")
    Esp = input()

    try:
        SQL.Actualizar_BD(
            """
                UPDATE PERSONAL SET
                NOMBRE = '%s',
                HORARIO  = '%s',
                INGRESO = '%s',
                ESPECIALIDAD = '%s'
                WHERE NUM_EMPL = '%s'
            """,
            (name,Hor,Ing,Esp,NE)
        )
    except Exception as e:
        print("Ocurrio el error: ",e)

        time.sleep(5)
        return

    print("\n\nPersonal actualizado con exito")
    time.sleep(1)

    return
    

def Elim_Per ():
    os.system("cls")
    print("Escriba el numero de empleado del personal que desea eliminar:", end = " ")
    NE = input()

    find = SQL.consulta_BD(
        """
            SELECT * FROM PERSONAL WHERE NUM_EMPL = '%s'
        """,
        (NE)
    )
    if not find:
        os.system("cls")
        print("El personal no esta registrado revise el numero de empleado")
        time.sleep(1)

        return

    try:
        SQL.Actualizar_BD(
            """
                DELETE FROM PERSONAL 
                WHERE NUM_EMPL = '%s'
            """,
            (NE)
        )
    except Exception as e:
        print("Ocurrio el error: ",e)

        time.sleep(5)
        return

    print("Personal borrado correctamente")
    time.sleep(1)

    return

def Hor_Per():
    os.system("cls")

    print("%-25s %8s %-30s   <-Turno Matutino" %("Nombre","Num. Emp","Especialidad",))

    find = SQL.consulta_BD(
        """
            SELECT NOMBRE, NUM_EMPL, ESPECIALIDAD FROM PERSONAL WHERE HORARIO = 'M'
        """,
        ()
    )
    if not find:
        print ("No hay Personal en este turno")
        time.sleep(1.5)
        
    else:
    
    
        for i in find:
            print("%-25s %8s %-30s" %i)

    print("\n\n%-25s %8s %-30s   <-Turno Vespertino" %("Nombre","Num. Emp","Especialidad",))

    find = SQL.consulta_BD(
        """
            SELECT NOMBRE, NUM_EMPL, ESPECIALIDAD FROM PERSONAL WHERE HORARIO = 'V'
        """,
        ()
    )
    if not find:
        print ("No hay Personal en este turno")
        time.sleep(1.5)
        
    else:
    
    
        for i in find:
            print("%-25s %8s %-30s" %i)
    input()   