#!/usr/bin/python3


"""
Script que cambia el nombre de un objeto State en la base de datos
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

    # Consulta el objeto State con ID igual a 2
    new_state = session.query(State).filter_by(id=2).first()

    # Cambia el nombre del objeto State a 'New Mexico'
    new_state.name = 'New Mexico'

    # Agrega el objeto State modificado a la sesión
    session.add(new_state)

    # Guarda los cambios en la base de datos
    session.commit()

    # Cierra la sesión
    session.close()
