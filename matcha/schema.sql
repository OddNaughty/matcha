create table if not EXISTS Users (
  id integer primary key NOT NULL,
  mail text not null UNIQUE,
  username text NOT NULL UNIQUE,
  password text not null,
  first_name text not null,
  last_name text not null,
  creation_time text NOT NULL DEFAULT(DATETIME('now', 'localtime'))
);
