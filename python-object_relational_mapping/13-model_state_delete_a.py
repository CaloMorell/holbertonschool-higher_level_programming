#!/usr/bin/python3

"""
Script que elimina objetos State de la base de datos que contienen la letra 'a'
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Obtiene los detalles de conexión MySQL desde los argumentos de la línea de comandos
    user = argv[1]
    password = argv[2]
    database = argv[3]

    # Crea un motor SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                        (user, password, database), pool_pre_ping=True)
    
    # Crea las tablas si no existen
    Base.metadata.create_all(engine)

    # Crea una sesión
    session = Session(engine)

    # Consulta todos los objetos State y elimina aquellos cuyos nombres contienen la letra 'a'
    deletes = session.query(State).order_by(State.id).all()
    for row in deletes:
        if 'a' in row.name:
            session.delete(row)

    # Guarda los cambios en la base de datos
    session.commit()

    # Cierra la sesión
    session.close()
