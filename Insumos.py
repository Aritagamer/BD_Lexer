import os
import time
import Conexion_SQL as SQL

#_____________________________________________________SUBMENU INSUMOS_____________________________________________________________
Ins = ['BIG ERROR','Medicamento','Instrumento','Aparato','Material']

def Alta_INS(tipo = 0):
    os.system("cls")
    print("Se procedera a dar de alta un %s espere" %(Ins[tipo]))
    time.sleep(1)
    os.system("cls")
    print("Porfavor Proporcione los datos que se le piden acontinuacion:",end = "\n\n")
       
    print("Nombre:",end = " ")
    name = input()
    print("Fecha de ingreso (DD/MM/AA):",end = " ")
    Ing = input()
    print("Area:",end = " ")
    Area = input()
    
    try:
        SQL.Actualizar_BD(
            """
                INSERT INTO INSUMOS (NOMBRE,INGRESO,AREA,TIPO) 
                VALUES ('%s' , '%s', '%s', '%s')
            """,
            (name,Ing,Area,tipo)
        )
    except Exception as e:
        print("Ocurrio el error: ",e)

        time.sleep(5)
        return

    print("\n\n%s dado de alta con exito"%(Ins[tipo]))
    time.sleep(1)

    return

def Mostr_INS (tipo = 0):
    os.system("cls")

    find = SQL.consulta_BD(
        """
            SELECT * FROM INSUMOS WHERE TIPO = '%s'
        """,
        (tipo)
    )
    if not find:
        print ("Nada que mostrar aun")
        time.sleep(1.5)
        return
    
    print("%-25s %5s %2s %10s %-30s" %("Nombre","ID","Tipo","Ingreso","Area",))
    
    for i in find:
        print("%-25s %5s %2s %10s %-30s" %i)
    input()

def Modif_INS (tipo = 0):
    os.system("cls")
    print("Escriba el ID del %s que desea modificar:" %( Ins[tipo] ), end = " ")
    ID = input()
    
    find = SQL.consulta_BD(
        """
            SELECT * FROM INSUMOS WHERE ID = '%s' AND TIPO = '%s'
        """,
        (ID,tipo)
    )
    if not find:
        os.system("cls")
        print("El %s no esta registrado revise el ID"%( Ins[tipo] ))
        time.sleep(1)

        return
    os.system("cls")
    
    print("Ingrese los nuevos datos del %s.\n\n" %( Ins[tipo] ))

    print("Nombre:",end = " ")
    name = input()
    print("Fecha de ingreso (DD/MM/AA):",end = " ")
    Ing = input()
    print("Area:",end = " ")
    Area = input()

    try:
        SQL.Actualizar_BD(
            """
                UPDATE PACIENTES SET
                NOMBRE = '%s',
                INGRESO  = '%s',
                AREA = '%s',
                WHERE ID = '%s' AND TIPO = '%s'
            """,
            (name,Ing,Area,ID,tipo)
        )
    except Exception as e:
        print("Ocurrio el error: ",e)

        time.sleep(5)
        return

    print("\n\n%s actualizado con exito"%( Ins[tipo] ))
    time.sleep(1)

    return
    

def Elim_INS (tipo = 0):
    os.system("cls")
    print("Escriba el ID del %s que desea eliminar:"%( Ins[tipo] ), end = " ")
    ID = input()

    find = SQL.consulta_BD(
        """
            SELECT * FROM INSUMOS WHERE ID = '%s' AND TIPO = '%s'
        """,
        (ID,tipo)
    )
    if not find:
        os.system("cls")
        print("El %s no esta registrado revise el ID"%( Ins[tipo] ))
        time.sleep(1)

        return

    try:
        SQL.Actualizar_BD(
            """
                DELETE FROM INSUMOS 
                WHERE ID = '%s' AND TIPO = '%s'
            """,
            (ID,tipo)
        )
    except Exception as e:
        print("Ocurrio el error: ",e)

        time.sleep(5)
        return

    print("%s borrado correctamente"%( Ins[tipo] ))
    time.sleep(1)

    return

