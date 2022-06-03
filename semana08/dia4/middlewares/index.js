const express  = require('express');
const morgan = require('morgan');

const app = express();

app.use(morgan('combined'))
app.use(function (req, res, next) {
    console.log('Time:', Date.now());
    next();
});

app.get("/",(req,res)=>{
    res.json({
        content:"ejemplo de middlewares"
    })
})

//middleware para una ruta

app.use('/usuario',function(req,res,next){
    console.log(a + 3);
    console.log('tipo request : ',req.method);
    next();
})

app.get("/usuario",(req,res)=>{
    res.json({
        nombre:'cesar'
    })
})

//MIDDLEWARE DE ERRORES
app.use(function(err,req,res,next){
    console.error(err.stack);
    res.status(500).json({
        status:false,
        content:'error en el servidor',
        detail:err.stack
    })
})

app.listen(5000,()=>console.log("http://localhost:5000"));