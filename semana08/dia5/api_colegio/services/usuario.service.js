const MysqlLib = require('../lib/mysql');
const bcrypt = require('bcryptjs');

class UsuarioService{

    constructor(){
        this.sql = new MysqlLib();
    }

    async getAll(){
        const sqlAll = "select * from tbl_usuario";
        const result = await this.sql.querySql(sqlAll);
        return result;
    }

    async create({usuario}){

        const passwordEncriptado = await bcrypt.hash(usuario.password,10);
        const sqlCreate = `insert into tbl_usuario(usuario_nombre,usuario_password)
                           values('${usuario.nombre}','${passwordEncriptado}')`;
        
        await this.sql.querySql(sqlCreate);
        const sqlUsuarioCreado = "select usuario_id as id,usuario_nombre as nombre from tbl_usuario order by usuario_id desc limit 1";
        const result = await this.sql.querySql(sqlUsuarioCreado);
        return result;
    }

}

module.exports = UsuarioService;