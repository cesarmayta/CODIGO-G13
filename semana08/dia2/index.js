const express = require('express');

const mysqlConnection = require('./database');

const app = express();
const port = 5000;

app.use(express.json());

app.get('/',function(req,res){
    res.json({
        'status':true,
        'content':'Bienvenido a mi API con express y nodemon'
    })
})

app.get('/alumno',function(req,res){
    mysqlConnection.query('select * from tbl_alumno',(err,rows,fields)=>{
        if(!err){
            res.json(rows);
        }else{
            console.log(err);
        }
    })
})

app.post('/alumno',function(req,res){
    const {nombre,email,celular,github} = req.body;
    const query = `insert into 
    tbl_alumno(alumno_nombre,alumno_email,alumno_celular,alumno_github) 
    values('${nombre}','${email}','${celular}','${github}')`;
    
    mysqlConnection.query(query,(err,rows,fields)=>{
        if(!err){
            res.json({
                'status':true,
                'content':'alumno creado'
            })
        }else{
            console.log(err);
        }
    })
    
})


app.put('/alumno/:id',function(req,res){
    const {nombre,email,celular,github} = req.body;
    const {id} = req.params;

    let query = "update tbl_alumno set alumno_nombre=?,alumno_email=?"
    query += ",alumno_celular=?,alumno_github=? where alumno_id=?"
    
    mysqlConnection.query(query,[nombre,email,celular,github,id],
        (err,rows,fields)=>{
            if(!err){
                res.json({
                    'status':true,
                    'content':'alumno actualizado'
                })
            }else{
                console.log(err);
            }
        })
})

app.delete('/alumno/:id',function(req,res){
    const {id} = req.params;

    query = "delete from tbl_alumno where alumno_id = ?"

    mysqlConnection.query(query,[id],(err,rows,fields)=>{
        if(!err){
            res.json({
                'status':true,
                'content':'alumno eliminado'
            })
        }else{
            console.log(err);
        }
    })
})

app.listen(port,()=>{
    console.log('Servidor iniciado en http://localhost:'+port);
})
