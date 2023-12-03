import sqlite3

conexion = sqlite3.connect(database='test_db')

cursor = conexion.cursor()

sentencia = 'SELECT * FROM PERSONA'

cursor.execute(sentencia)
