#!/usr/bin/python3

"""script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.id == 2).update({'name': 'New Mexico'})
    session.commit()

    session.close()
