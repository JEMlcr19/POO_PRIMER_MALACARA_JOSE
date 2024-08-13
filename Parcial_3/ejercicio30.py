import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="utd2024",
    database="escolares"
)


cursor = conexion.cursor()


sql_insert = "INSERT INTO alumnos (nombre, edad) VALUES (%s, %s)"
valores_insert = ("Jessica", "19")
cursor.execute(sql_insert, valores_insert)
conexion.commit()

sql_select = "SELECT * FROM alumnos"
cursor.execute(sql_select)
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)


sql_update = "UPDATE maestros SET materia = %s WHERE materia = ?"
valores_update = ("Materia", "POO")
cursor.execute(sql_update, valores_update)
conexion.commit()

sql_delete = "DELETE FROM alumnos WHERE edad = 15"
valores_delete = ("edad",)
cursor.execute(sql_delete)
conexion.commit()

cursor.close()
conexion.close()