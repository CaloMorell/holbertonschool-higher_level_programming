#!/usr/bin/python3
"""
Script selects states that match a user input
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Verifica si se proporciona el número correcto de argumentos de línea de comandos

        # Obtiene los detalles de la conexión MySQL, y el nombre del estado a buscar desde los argumentos de la línea de comandos
        user = argv[1]
        password = argv[2]
        database = argv[3]
        name = argv[4]

        # Establece una conexión con la base de datos MySQL
        db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=database)

        # Crea un objeto cursor para ejecutar consultas SQL
        cur = db.cursor()

        # Usa el formato para crear la consulta SQL con la entrada del usuario para el nombre del estado
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(name)
        
        # Ejecuta la consulta SQL
        cur.execute(query)

        # Obtiene todas las filas devueltas por la consulta SQL
        rows = cur.fetchall()

        # Imprime los resultados
        for row in rows:
            print(row)

        # Cierra el cursor para liberar recursos
        cur.close()

        # Cierra la conexión a la base de datos
        db.close()
