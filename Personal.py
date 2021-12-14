import os
import time

def Alta_Per():
    os.system("cls")
    print("Se procedera a dar de alta al nuevo Personal espere")
    time.sleep(1)
    os.system("cls")
    print("Porfavor Proporcione los datos que se le piden acontinuacion:",end = "\n\n")
    print("Nombre (Apellido Paterno, Materno, Nombre):",end = " ")
    name = input()
    print("Numero de Empleado:",end = " ")
    Num_Emp = input()
    print("Horario de Trabajo:",end = " ")
    Hor = input()
    print("Fecha de ingreso:",end = " ")
    Ingr = input()
    print("Especialidad:",end = " ")
    Esp = input()
    


    print("\n\nNuevo Personal dado de alta con exito")
    time.sleep(1)

    return  