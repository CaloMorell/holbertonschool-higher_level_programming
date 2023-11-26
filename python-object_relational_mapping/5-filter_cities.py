#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Obtiene los detalles de la conexión MySQL y el nombre del estado desde los argumentos de la línea de comandos
    user = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]
    cities = []  # Inicializa una lista vacía para almacenar los nombres de las ciudades

    # Establece una conexión con la base de datos MySQL
    db = MySQLdb.connect(host='localhost', port=3306, user=user, passwd=password, db=database)

    # Crea un objeto cursor para ejecutar consultas SQL
    cur = db.cursor()

    # Ejecuta una consulta SQL para obtener información de las ciudades desde las tablas 'cities' y 'states' para el estado especificado
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name=%s ORDER BY id ASC""", (state,))

    # Obtiene todas las filas devueltas por la consulta SQL
    rows = cur.fetchall()

    # Añade los nombres de las ciudades a la lista 'cities'
    for row in rows:
        cities.append(row[1])

    # Imprime la lista de nombres de ciudades, separados por comas
    print(', '.join(cities))

    # Cierra el cursor para liberar recursos
    cur.close()

    # Cierra la conexión a la base de datos
    db.close()
