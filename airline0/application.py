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


if __name__ == "__main__":
    main()
