"""
Script que lista todos los objetos State de la base de datos
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

    # Consulta e imprime todos los objetos State, ordenados por id
    states = session.query(State).order_by(State.id.asc()).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Cierra la sesión
    session.close()
