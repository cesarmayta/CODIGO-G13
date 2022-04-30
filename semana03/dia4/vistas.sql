select * from tbl_matricula_curso;

CREATE VIEW vw_matricula_notas AS
select 
m.matricula_fecha_registro as fecha,
a.alumno_nombre as alumno,
c.curso_nombre as curso,
mc.curso_nota as nota
from tbl_matricula_curso mc
inner join tbl_matricula m ON mc.matricula_id = m.matricula_id
inner join tbl_alumno a ON m.alumno_id = a.alumno_id
inner join tbl_curso c ON mc.curso_id = c.curso_id
;

select alumno,curso from vw_matricula_notas;
