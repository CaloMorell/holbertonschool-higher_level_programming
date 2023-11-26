#!/usr/bin/python3
"""
Script that selects states based on user input while avoiding SQL injection
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Obtiene los detalles de la conexión MySQL y el nombre
    del estado desde los argumentos de la línea de comandos"""
    user = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]

    """Establece una conexión con la base de datos MySQL"""
    db = MySQLdb.connect(
        host='localhost', port=3306, user=user,
        passwd=password, db=database)

    """Crea un objeto cursor para ejecutar consultas SQL"""
    cur = db.cursor()

    """Utiliza una consulta parametrizada
    para evitar la inyección SQL"""
    cur.execute(
        "SELECT * FROM states WHERE name=%s ORDER BY id ASC", (name,))

    """Obtiene todas las filas devueltas por la consulta SQL"""
    rows = cur.fetchall()

    """Imprime los resultados"""
    for row in rows:
        print(row)

    """Cierra el cursor para liberar recursos"""
    cur.close()

    """Cierra la conexión a la base de datos"""
    db.close()
