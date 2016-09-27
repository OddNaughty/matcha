drop TABLE users;
create table if not EXISTS Users (
  id SERIAL primary key NOT NULL ,
  mail VARCHAR(254) not null UNIQUE,
  username VARCHAR(100) NOT NULL UNIQUE,
  password CHAR(64) not null,
  first_name VARCHAR(100) not null,
  last_name VARCHAR(100) not null,
  creation_time TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);
