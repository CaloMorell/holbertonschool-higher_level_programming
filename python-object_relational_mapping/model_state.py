"""
State class
"""

# Importa SQLAlchemy y los módulos necesarios
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Crea una base declarativa
Base = declarative_base()

# Define la clase State que hereda de la base declarativa
class State(Base):
    """
    State class
    """
    # Nombre de la tabla en la base de datos
    __tablename__ = 'states'

    # Definición de columnas
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
