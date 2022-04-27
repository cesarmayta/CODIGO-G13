CREATE TABLE alumno (
  id int(11) NOT NULL AUTO_INCREMENT,
  nombres varchar(100) NOT NULL,
  apellidos varchar(100) NOT NULL,
  email varchar(100) NOT NULL,
  pais varchar(100) DEFAULT 'Perú',
  nota int(11) DEFAULT '0',
  PRIMARY KEY (id)
)