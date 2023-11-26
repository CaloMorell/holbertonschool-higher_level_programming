#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Obtiene los detalles de la conexión MySQL desde los argumentos de la línea de comandos
    user = argv[1]
    password = argv[2]
    database = argv[3]

    # Establece una conexión con la base de datos MySQL
    db = MySQLdb.connect(host='localhost', port=3306, user=user, passwd=password, db=database)

    # Crea un objeto cursor para ejecutar consultas SQL
    cur = db.cursor()

    # Ejecuta una consulta SQL para obtener información de las ciudades desde las tablas 'cities' y 'states'
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id
                ORDER BY id ASC""")

    # Obtiene todas las filas devueltas por la consulta SQL
    rows = cur.fetchall()

    # Imprime los resultados
    for row in rows:
        print(row)

    # Cierra el cursor para liberar recursos
    cur.close()

    # Cierra la conexión a la base de datos
    db.close()
