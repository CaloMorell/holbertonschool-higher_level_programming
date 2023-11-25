#!/usr/bin/python3

#Este script mostrara los estados ordenados por ID de forma ascendente.

import MySQLdb

from sys import argv
if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=database)


    cur = db.cursor()
    cur.execute("SELECT * FORM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    
    cur.close()
    db.close()
