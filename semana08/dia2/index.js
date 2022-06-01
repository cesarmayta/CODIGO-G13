const express = require('express');

const app = express();
const port = 5000;

app.get('/',function(req,res){
    res.json({
        'status':true,
        'content':'Bienvenido a mi API con express y nodemon'
    })
})

app.listen(port,()=>{
    console.log('Servidor iniciado en http://localhost:'+port);
})
