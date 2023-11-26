#!/usr/bin/python3

"""
Script que agrega un objeto State a la base de datos
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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format (user, password, database), pool_pre_ping=True)
    
    # Crea las tablas si no existen
    Base.metadata.create_all(engine)

    # Crea una sesión
    session = Session(engine)

    # Crea un nuevo objeto State con el nombre "Louisiana"
    new_state = State(name="Louisiana")

    # Agrega el nuevo objeto State a la sesión
    session.add(new_state)

    # Guarda los cambios en la base de datos
    session.commit()

    # Imprime el ID asignado al nuevo objeto State después de ser agregado a la base de datos
    print(new_state.id)

    # Cierra la sesión
    session.close()
