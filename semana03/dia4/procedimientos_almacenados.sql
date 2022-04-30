DELIMITER $$
CREATE PROCEDURE sp_matricular_alumno(IN alu_id INT,IN niv_id INT,IN mod_id INT)
BEGIN
    --variables
    DECLARE matId INT;
    DECLARE curId INT;
    set matId = 0;
    set curId = 1;

    --insertar datos en la tabla matricula
    insert into tbl_matricula(alumno_id,nivel_id,modulo_id)
    values (alu_id,niv_id,mod_id);

    select max(matricula_id) into matId from tbl_matricula;

    WHILE curId <= 6 DO
        insert into tbl_matricula_curso(matricula_id,curso_id)
        values (matId,curId);

        SET curId = curId + 1;

    END WHILE;
END
$$

DELIMITER ;

CALL sp_matricular_alumno(4,1,1);

select * from tbl_matricula;

select * from tbl_matricula_curso;