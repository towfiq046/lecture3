import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://postgres:5504655@localhost/lecture3')
db = scoped_session(sessionmaker(bind=engine))  # multiple users


def main():
    flights = db.execute("SELECT origin, destination, duration from flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes. ")


if __name__ == "__main__":
    main()
