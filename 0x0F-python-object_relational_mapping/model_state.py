#!/usr/bin/python3

"""Creates the State Model and Table"""

from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL


Base = declarative_base()


class State(Base):
    """
    State class

    Attributes:
        __tablename__ (str): The table mapped to State class
        id (int): The state id
        name (str): The name of the state
    """

    __tablename__ = 'states'

    id = Column(Integer, Sequence('state_id_seq'), autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
