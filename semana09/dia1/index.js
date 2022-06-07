const express = require('express');
const app = express();

app.get("/",(req,res)=>{
    res.json({
        content:'servidor activo'
    })
})

const port =5000;
app.listen(port,()=>console.log('servidor en http://localhost:'+port));

/************* TRABAJANDO CON SEQUELIZE ************/
const Sequelize = require('sequelize');

const sequelize = new Sequelize({
    dialect:'sqlite',
    storage: './database.sqlite'
})

sequelize.authenticate()
.then(()=>{
    console.log("Conexón establecida")
})
.catch(err=>{
    console.log("error : " + err)
})

//creamos modelos
const Alumnos = sequelize.define(
    'alumnos',
    {
        nombre:Sequelize.STRING,
        email:Sequelize.STRING
    }
)

//migraciones
/*
sequelize.sync({force:true})
.then(()=>{
    console.log("tablass migradas");
    Alumnos.bulkCreate(
        [
            {nombre:'cesar mayta',email:'cesarmayta@gmail.com'},
            {nombre:'Claudia Gonzales',email:'claudia@gmail.com'}
        ]
    ).then(function(){
        return Alumnos.findAll();
    }).then(function(alumnos){
        console.log(alumnos);
    })
})
*/
//CREACIÓN DE ENDPOINTS
app.get('/alumno',(req,res)=>{
    Alumnos.findAll()
    .then(
        alumnos => res.json(alumnos)
    )
})

app.use(express.json());

app.post('/alumno',(req,res)=>{
    Alumnos.create(
        {
            nombre: req.body.nombre,
            email: req.body.email
        }
    ).then(function(alumnos){
        res.json(alumnos);
    })
})

app.put('/alumno/:id',(req,res)=>{
    Alumnos.findByPk(req.params.id)
    .then(function(alumnos){
        alumnos.update({
            nombre:req.body.nombre,
            email:req.body.email
        }).then(function(alumnos){
            res.json(alumnos);
        })
    })
})

app.delete('/alumno/:id',(req,res)=>{
    Alumnos.findByPk(req.params.id)
    .then(function(alumnos){
        alumnos.destroy();
    }).then(function(alumnos){
        res.sendStatus(201);
    })
})

