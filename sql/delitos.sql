create database delitos;
\c delitos\;
create table delitos(
  index int,
  fecha date,
  franja_horaria varchar(500),
  barrio varchar(500),
  delitos varchar(500),
  id_comuna varchar(500),
  anio int,
  mes int,
  dia_semana varchar(500),
  horario varchar(500),
  primary key (index)
);

