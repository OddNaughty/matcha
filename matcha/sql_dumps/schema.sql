DROP TABLE Users;
DROP TABLE Genders;

CREATE TABLE IF NOT EXISTS Genders (
  id SERIAL PRIMARY KEY NOT NULL ,
  name VARCHAR(254) NOT NULL UNIQUE
);


create table if not EXISTS Users (
  id SERIAL primary key NOT NULL ,
  mail VARCHAR(254) not null UNIQUE,
  username VARCHAR(100) NOT NULL UNIQUE,
  password CHAR(97) not null,
  first_name VARCHAR(100) not null,
  last_name VARCHAR(100) not null,
  creation_time TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  gender_id INTEGER REFERENCES Genders (id)
);
