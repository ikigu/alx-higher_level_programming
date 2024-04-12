#!/usr/bin/python3

"""
Write a script that prints the State object
with the name passed as argument from the database hbtn_0e_6_usa

Requirements:
    - Your script should take 4 arguments: mysql username,
    mysql password, database name and state name
    to search (SQL injection free)
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state -
    >>> from model_state import Base, State
    - Your script should connect to a MySQL server running
    on localhost at port 3306
    - You can assume you have one record with the state name to search
    - Results must display the states.id
    - If no state has the name you searched for, display Not found
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

    state_name_search_term = argv[4]

    state = session.query(State).filter(
        State.name.like(f'%{state_name_search_term}%')).order_by(
            State.id).first()

    if state is not None:
        print(f'{state.id}')
    else:
        print('Not found')
