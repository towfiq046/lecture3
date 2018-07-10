import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgresql://postgres:5504655@localhost/lecture3")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    flights = db.execute("SELECT * from flights").fetchall()
    return render_template("index.html", flights = flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    #get form informationself.
    name = request.form.get("name")
    try:
        flightID = int(request.form.get("flightID"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")


    #make sure flight exist.
    if db.execute("SELECT * from flights where id = :id", {"id": flightID}).rowcount == 0:
        return render_template("error.html", message="No such flight with that id. ")
    db.execute("INSERT INTO passengers (name, flightID) values (:name, :flightID)",
            {"name": name, "flightID": flightID})
    db.commit()
    return render_template("success.html")

@app.route("/flights")
def flights():
    """list all flights"""
    flights = db.execute("SELECT * from flights").fetchall()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flightID>")
def flight(flightID):
    """lists detail about a single flight."""

    #make sure flight exists.
    flight = db.execute("SELECT * from flights where id = :id", {"id": flightID}).fetchone()
    if flight is None:
        return render_template("error.html", message="No such flights.")

    #get all passengersself.
    passengers = db.execute("SELECT name from passengers where flightID = :flightID",
                            {"flightID": flightID}).fetchall()
    return render_template("flight.html", flight=flight, passengers=passengers)


if __name__ == "__main__":
    main()
