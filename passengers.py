import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:5504655@localhost/lecture3")
db = scoped_session(sessionmaker(bind=engine))


def main():

    # list all flights.
    flights = db.execute("SELECT * from flights").fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination} in {flight.duration} minutes.")

    # prompt user to choose a flight.
    flightID = int(input("\nFlight ID : "))
    flight = db.execute("SELECT origin, destination, duration from flights where id = :id",
                        {"id": flightID}).fetchone()

    # valid flight id.
    if flight is None:
        print("Error: No such flight.")
        return

    # list passengers
    passengers = db.execute("SELECT name from passengers where flightID = :flightID",
                            {"flightID": flightID}).fetchall()
    print("\nPassengers: ")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No passenger.")


if __name__ == "__main__":
    main()
