#!/usr/bin/python3
"""
Write a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa


"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':

    # Collect data from argv arguments
    username = argv[1]
    passwd = argv[2]
    db = argv[3]

    # Make connection
    engine = create_engine(
        f'mysql+mysqldb://{username}:{passwd}@localhost:3306/{db}'
        )

    # Make 'cursor'
    session = sessionmaker(bind=engine)
    session = session()

    new_state = State(name='Louisiana')

    session.add(new_state)
    session.commit()  # Commit the transaction

    states = session.query(State).filter(State.name == "Louisiana").all()
    [print(f"{state.id}") for state in states]

    session.close()
