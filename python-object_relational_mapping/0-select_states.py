#!/usr/bin/python3

"""
Script que muestra los estados ordenados por id de forma ascendente
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Obtén los detalles de la conexión MySQL desde los argumentos de la línea de comandos
    user = argv[1]
    password = argv[2]
    database = argv[3]

    # Conéctate a la base de datos MySQL
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                        passwd=password, db=database)

    # Crea un cursor para ejecutar consultas SQL
    cur = db.cursor()

    # Ejecuta la consulta SQL para seleccionar todos los estados ordenados por id de forma ascendente
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Obtiene todos los resultados de la consulta
    rows = cur.fetchall()

    # Itera sobre los resultados e imprime cada fila
    for row in rows:
        print(row)

    # Cierra el cursor y la conexión a la base de datos
    cur.close()
    db.close()
