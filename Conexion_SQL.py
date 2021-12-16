import sqlite3 as SQL



#Conexion = SQL.connect()
#Cursor = Conexion.cursor()


def consulta_BD(*args):

	Conect=SQL.connect("./Hospital.db")

	Curs=Conect.cursor()
	#print(args[0])
	Curs.execute(args[0] % args[1])

	Res=Curs.fetchall()

	Conect.commit()
	Conect.close()



	return Res

def Actualizar_BD(*args):

	Conect=SQL.connect("./Hospital.db")

	Curs=Conect.cursor()

	Curs.execute(args[0] % args[1])

	Conect.commit()

	Conect.close()