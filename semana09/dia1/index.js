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