#!/usr/bin/python3

"""Creates the State Model and Table"""

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, Sequence('state_id_seq'), autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
