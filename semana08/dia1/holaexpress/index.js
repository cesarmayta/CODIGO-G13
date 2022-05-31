const express = require('express');

const app = express();
const port = 5000;

app.get('/',(req,res)=>{
    res.send('<center><h1>BIENVENIDO A MI SITIO WEB CON EXPRESS</h1></center>');
})

app.get('/hola/:nombre',(req,res)=>{
    res.send('<center><h1>HOLA  '+ req.params.nombre +'</h1></center>');
})

app.get('/saludojson',(req,res)=>{
    res.json({
        'saludo':'hola'
    })
})

app.listen(port,function(){
    console.log("servidor activo en http://localhost:"+port);
})