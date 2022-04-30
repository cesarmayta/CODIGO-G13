insert into tbl_matricula(matricula_fecha_registro,alumno_id,nivel_id,modulo_id)
select CURRENT_TIMESTAMP,alumno_id,
(select nivel_id from tbl_nivel limit 1),
(select modulo_id from tbl_modulo limit 1)
 from tbl_alumno;

