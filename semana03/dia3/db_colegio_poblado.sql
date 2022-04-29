--poblado de datos
--ALUMNO
insert into tbl_alumno(alumno_nombre,alumno_email,alumno_celular,alumno_github)
VALUES
('César Mayta','cesarmayta@gmail.com','956290589','https://github.com/cesarmayta'),
('Susana Perez','susanaperez@hotmail.com','234234234','https://github.com/susanaperez'),
('Claudia Loza','claudialoza@yahoo.com','343434767','https://github.com/claudialoza'),
('Anibal Ruiz','anibalruiz@gmail.com','966766767','https://github.com/anibalruiz'),
('Jorge Contreras','jorgecontreras@gmail.com','2332323','https://github.com/jorgecontreras');

-- CURSO
insert into tbl_curso(curso_nombre)
VALUES
('HTML Y CSS'),('JAVASCRIPT'),('REACT.JS'),('PYTHON'),('MYSQL'),('FLASK');

--EVALUACIONES
insert into tbl_evaluacion(evaluacion_nombre)
VALUES
('PROYECTO CURSO');

--MODULO
insert into tbl_modulo(modulo_nombre,modulo_fecha_inicio,modulo_nro_sesiones)
VALUES
('FRONT END','2022-01-01',15),
('BACKEND','2022-03-01',15);

--NIVEL
insert into tbl_nivel(nivel_nombre)
VALUES
('BASICO'),('AVANZADO');
