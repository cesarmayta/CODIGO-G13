const mysql = require('mysql');

const mysqlConnection = mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'',
    database:'db_colegio'
});

mysqlConnection.connect(function (err){
    if(err){
        console.error(err);
        return;
    }
    else{
        console.log('conectado a la base de datos')
    }
});

module.exports = mysqlConnection;
 
/*mysqlConnection.query('select * from tbl_alumno', function (error, results, fields) {
  if (error) throw error;
  console.log(results);
});*/
 
