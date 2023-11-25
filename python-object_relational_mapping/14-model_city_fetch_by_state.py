#!/usr/bin/python3

"""
Script que lista todos los objetos City de la base de datos
"""

from sys import argv
from model_state import Base, State
from model_city import City
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

    # Consulta todos los objetos City junto con el nombre del estado al que pertenecen
    new_table = session.query(City, State)\
                .filter(City.state_id == State.id)\
                .order_by(City.id.asc()).all()

    # Itera sobre los resultados e imprime el nombre del estado, el ID y el nombre de la ciudad
    for cities, states in new_table:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))

    # Cierra la sesión
    session.close()
