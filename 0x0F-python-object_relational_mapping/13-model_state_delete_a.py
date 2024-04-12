"""
Write a script that deletes all State objects
with a name containing the letter a from the database hbtn_0e_6_usa

Requirements:
    - Your script should take 3 arguments:
      mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state
      >>> from model_state import Base, State
    - Your script should connect to a MySQL server
      running on localhost at port 3306
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

    states_with_letter_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for instance in states_with_letter_a:
        session.delete(instance)

    session.commit()
