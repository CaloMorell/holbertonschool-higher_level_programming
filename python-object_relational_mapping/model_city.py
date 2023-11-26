#!/usr/bin/python3

"""
City class
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import relationship

class City(Base):
    """
    City class
    """
    # Nombre de la tabla en la base de datos
    __tablename__ = 'cities'

    # Columnas de la tabla
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

    # Relación con la tabla State
    state = relationship(State, back_populates="cities")
