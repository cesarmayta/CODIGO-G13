const MysqlLib = require('../lib/mysql.lib');

class ClienteService{

    constructor(){
        this.sql = new MysqlLib();
    }

    async getAll(){
        const sqlAll = `SELECT 
                        cli.id as id,
                        usu.username as usuario,
                        usu.first_name as nombres,
                        usu.last_name as apellidos,
                        usu.email as email,
                        cli.direccion as direccion,
                        cli.telefono as telefono 
                        FROM tienda_cliente cli
                        INNER JOIN auth_user usu on cli.usuario_id = usu.id
                        `;
        const result = await this.sql.querySql(sqlAll);
        return result;
    }

}

module.exports = ClienteService;