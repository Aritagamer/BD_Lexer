import os
import time

def Alta_Pac():
    os.system("cls")
    print("Se procedera a dar de alta a un paciente espere")
    time.sleep(1)
    os.system("cls")
    print("Porfavor Proporcione los datos que se le piden acontinuacion:",end = "\n\n")
    print("Nombre (Apellido Paterno, Materno, Nombre):",end = " ")
    name = input()
    print("Numero de Seguro Social:",end = " ")
    NSS = input()
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


    print("\n\nPaciente dado de alta con exito")
    time.sleep(1)

    return

def Mostr_Pac ():
    os.system("cls")
    print ("Nada que mostrar aun")
    time.sleep(1)

def Modif_Pac ():
    os.system("cls")
    print("Escriba el numero de seguro social del paciente que desea modificar:", end = " ")
    NSS = input()
    time.sleep(1)

def Elim_Pac ():
    os.system("cls")
    print("Escriba el numero de seguro social del paciente que desea eliminar:", end = " ")
    NSS = input()
    time.sleep(1)