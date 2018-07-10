insert into flights (origin, destination, duration) values ('Khulna', 'Pakistan', 890);
insert into flights (origin, destination, duration) values ('Dhaka', 'Riyad', 2110);
insert into flights (origin, destination, duration) values ('Barisal', 'India', 890);
insert into flights (origin, destination, duration) values ('Qatar', 'Paris', 1150);
insert into flights (origin, destination, duration) values ('Khulna', 'Jeddah', 2250);
insert into flights (origin, destination, duration) values ('Dhaka', 'Brasil', 1800);

update flights
  set duration = 1700
  where origin = 'Dhaka'
  and destination = 'Brasil';

** SELECT * from flights where origin like '%a%';

** delete from flights where destination = 'Paris';

** SELECT * from flights limit 2;

** SELECT * from flights order by duration asc;

** SELECT origin, count(*) from flights group by origin;

** SELECT origin, count(*) from flights group by origin having count(*) > 1;

CREATE TABLE passengers (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  flightID INTEGER references flights
);


insert into passengers (name, flightID) values ('Sujon', 6);
insert into passengers (name, flightID) values ('Sakib', 3);
insert into passengers (name, flightID) values ('Ratul', 6);
insert into passengers (name, flightID) values ('Anik', 3);
insert into passengers (name, flightID) values ('AUhid', 8);
insert into passengers (name, flightID) values ('Towfiq', 4);


SELECT origin, destination, name from flights join passengers on
passengers.flightID = flights.id;

SELECT origin, destination, name from flights join passengers on
passengers.flightID = flights.id where name = 'Sujon';

SELECT origin, destination, name from flights left join passengers on
passengers.flightID = flights.id; // left table will b in full form.


SELECT flightID from passengers group by flightID having count(*) > 1;

//nested:
SELECT * from flights where id in
(SELECT flightID from passengers group by flightID having count(*) > 1);

** delete from passengers where name='Towfiq';
