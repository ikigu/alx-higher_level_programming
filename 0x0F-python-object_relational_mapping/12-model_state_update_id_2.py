#!/usr/bin/python3

"""
Write a script that changes the name
of a State object from the database hbtn_0e_6_usa

Requirements:
    - Your script should take 3 arguments:
      mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state
      >>> from model_state import Base, State
    - Your script should connect to a MySQL server
      running on localhost at port 3306
    - Change the name of the State where id = 2 to New Mexico
    - Your code should not be executed when imported
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    sql_db = {
        'drivername': 'mysql+mysqldb',
        'host': 'localhost',
        'port': 3306,
        'username': argv[1],
        'password': argv[2],
        'database': argv[3]
    }

    engine = create_engine(URL.create(**sql_db))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=2).first()
    state.name = 'New Mexico'
    session.commit()
