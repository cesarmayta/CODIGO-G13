const express = require('express');
const {config} = require('../config');
const cors = require('cors');

const app = express();

app.use(cors());
app.use(express.json());

app.get('/',(req,res)=>{
    res.json({
        status:true,
        content:'ms cliente activo'
    })
})

const clienteApi = require('../routes/cliente.route');
clienteApi(app);

app.listen(config.ms_clientes.port,function(){
    console.log("ms clientes : http://localhost:"+config.ms_clientes.port);
})
