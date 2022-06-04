const MysqlLib = require('../lib/mysql');
const bcrypt = require('bcryptjs');

class UsuarioService{

    constructor(){
        this.sql = new MysqlLib();
    }

    async getAll(){
        const sqlAll = "select usuario_id as id,usuario_nombre as usuario from tbl_usuario";
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

    async validate({usuario}){

        const sqlPwdUsuario = `select usuario_id as id,usuario_password as pwd from tbl_usuario where usuario_nombre ='${usuario.usuario}'`;
        console.log("paso 2 ) sql para buscar el id y password encriptado en la base de datos : \n" + sqlPwdUsuario);
        const result = await this.sql.querySql(sqlPwdUsuario);
        console.log("paso 3 ) comparamos el password de la base de datos  : \n" + result[0].pwd + "\n con el password enviado por el post \n" + usuario.password);
        if(await bcrypt.compare(usuario.password,result[0].pwd)){
            //si la comparación es exitosa cargara los datos del usuario
            /*const sqlUsuarioEncontrado = `select usuario_id as id,usuario_nombre as usuario from tbl_usuario where usuario_id='${result[0].id}'`;
            console.log("sql usuario encontrado : \n" + sqlUsuarioEncontrado);
            const resultUsuarioEncontrado = await this.sql.querySql(sqlUsuarioEncontrado);
            console.log("json usuario encontrado : \n" + resultUsuarioEncontrado[0]);
            return resultUsuarioEncontrado[0];*/
            const usuarioFound = {
                id:result[0].id,
                usuario:usuario.nombre
            }
            return usuarioFound;
        }else{
            const usuarioNotFound = {
                id:0,
                usuario:'usuario no valido'
            }
            return usuarioNotFound;
        }

    }

}

module.exports = UsuarioService;