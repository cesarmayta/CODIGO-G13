CREATE TABLE alumno(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(200)
);

ALTER TABLE alumno
ADD COLUMN pais VARCHAR(100) DEFAULT 'Perú';
