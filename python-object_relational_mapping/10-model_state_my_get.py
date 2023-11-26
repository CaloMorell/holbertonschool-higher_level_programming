#!/usr/bin/python3

"""
Script que imprime el objeto State con el nombre proporcionado como argumento
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Obtiene los detalles de conexión MySQL y el nombre del estado desde los argumentos de la línea de comandos
    user = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]

    # Crea un motor SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format (user, password, database), pool_pre_ping=True)
    
    # Crea las tablas si no existen
    Base.metadata.create_all(engine)

    # Crea una sesión
    session = Session(engine)

    # Consulta el objeto State con el nombre proporcionado
    state = session.query(State).filter(State.name == name).first()

    # Imprime el ID del objeto State si existe, de lo contrario, imprime "Not found"
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Cierra la sesión
    session.close()
