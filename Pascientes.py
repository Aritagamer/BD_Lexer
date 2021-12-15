import os
import time
import Conexion_SQL as SQL

#_____________________________________________________SUBMENU LISTA PACIENTES_____________________________________________________________

def Alta_Pac():
    os.system("cls")
    print("Se procedera a dar de alta a un paciente espere")
    time.sleep(1)
    os.system("cls")
    print("Porfavor Proporcione los datos que se le piden acontinuacion:",end = "\n\n")
    
    print("Numero de Seguro Social:",end = " ")
    NSS = input()
    
    find = SQL.consulta_BD(
        """
            SELECT * FROM PACIENTES WHERE NSS = %s
        """,
        (NSS)
    )
    if find:
        os.system("cls")
        print("Paciente registrado con anterioridad revise el numero de seguro social")
        time.sleep(1)

        return
    
    print("Nombre (Apellido Paterno, Materno, Nombre):",end = " ")
    name = input()
    print("Numero de Historial:",end = " ")
    Hist = input()
    print("Telefono:",end = " ")
    Tel = input()
    print("Domicilio:",end = " ")
    Dom = input()
    print("Observaciones:",end = " ")
    Obs = input()
    print("Motivos:",end = " ")
    Mot = input()

    try:
        SQL.Actualizar_BD(
            """
                INSERT INTO PACIENTES 
                VALUES ('%s' , '%s', '%s', '%s', '%s', '%s', '%s')
            """,
            (name,NSS,Hist,Tel,Dom,Obs,Mot)
        )
    except Exception as e:
        print("Ocurrio el error: ",e)

        time.sleep(5)
        return

    print("\n\nPaciente dado de alta con exito")
    time.sleep(1)

    return

def Mostr_Pac ():
    os.system("cls")

    find = SQL.consulta_BD(
        """
            SELECT * FROM PACIENTES
        """,
        ()
    )
    if not find:
        print ("Nada que mostrar aun")
        time.sleep(1.5)
        return
    
    print("%-25s %8s %10s %10s %-30s %-50s %-50s" %("Nombre","NSS","Hist.","Tel.","Domicilio","Observaciones","Motivos",))
    
    for i in find:
        print("%-25s %8s %10s %10s %-30s %-50s %-50s" %i)
    input()

def Modif_Pac ():
    os.system("cls")
    print("Escriba el numero de seguro social del paciente que desea modificar:", end = " ")
    NSS = input()
    
    find = SQL.consulta_BD(
        """
            SELECT * FROM PACIENTES WHERE NSS = %s
        """,
        (NSS)
    )
    if not find:
        os.system("cls")
        print("El paciente no esta registrado revise el numero de seguro social")
        time.sleep(1)

        return
    os.system("cls")
    
    print("Ingrese los nuevos datos del paciente.\n\n")

    print("Nombre (Apellido Paterno, Materno, Nombre):",end = " ")
    name = input()
    print("Numero de Historial:",end = " ")
    Hist = input()
    print("Telefono:",end = " ")
    Tel = input()
    print("Domicilio:",end = " ")
    Dom = input()
    print("Observaciones:",end = " ")
    Obs = input()
    print("Motivos:",end = " ")
    Mot = input()

    try:
        SQL.Actualizar_BD(
            """
                UPDATE PACIENTES SET
                NOMBRE = '%s',
                HIST  = '%s',
                TEL = '%s',
                DOM = '%s',
                OBSERV = '%s',
                MOTIVOS = '%s'
                WHERE NSS = '%s'
            """,
            (name,Hist,Tel,Dom,Obs,Mot,NSS)
        )
    except Exception as e:
        print("Ocurrio el error: ",e)

        time.sleep(5)
        return

    print("\n\nPaciente actualizado con exito")
    time.sleep(1)

    return
    

def Elim_Pac ():
    os.system("cls")
    print("Escriba el numero de seguro social del paciente que desea eliminar:", end = " ")
    NSS = input()

    find = SQL.consulta_BD(
        """
            SELECT * FROM PACIENTES WHERE NSS = %s
        """,
        (NSS)
    )
    if not find:
        os.system("cls")
        print("El paciente no esta registrado revise el numero de seguro social")
        time.sleep(1)

        return

    try:
        SQL.Actualizar_BD(
            """
                DELETE FROM PACIENTES 
                WHERE NSS = '%s'
            """,
            (NSS)
        )
    except Exception as e:
        print("Ocurrio el error: ",e)

        time.sleep(5)
        return

    print("Paciente borrado correctamente")
    time.sleep(1)

    return





#_____________________________________________________SUBMENU CITAS_____________________________________________________________
def Gen_cita():
    pass

def Mos_cita():
    pass

def Mod_cita():
    pass

def Elim_cita():
    pass