const MysqlLib = require('../lib/mysql');

class CursoService{

    constructor(){
        this.sql = new MysqlLib();
    }

    async getAll(){
        const sqlAll = "select * from tbl_curso";
        const result = await this.sql.querySql(sqlAll);
        return result;
    }

}

module.exports = CursoService;