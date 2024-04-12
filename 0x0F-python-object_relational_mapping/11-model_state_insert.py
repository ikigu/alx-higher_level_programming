#!/usr/bin/python3

"""
Write a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa

Requirements:
    - Your script should take 3 arguments:
      mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state
      >>> from model_state import Base, State
    - Your script should connect to a MySQL server
      running on localhost at port 3306
    - Print the new states.id after creation
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    lousiana = session.query(State).filter(State.name == 'Louisiana').first()

    print(lousiana.id)
