const express = require('express');
const {config} = require('../config');
const cors = require('cors');

const app = express();

app.use(cors());
app.use(express.json());

app.get('/',(req,res)=>{
    res.json({
        status:true,
        content:'ms pedido activo'
    })
})

const pedidoApi = require('../routes/pedido.route');
pedidoApi(app);

app.listen(config.ms_pedidos.port,function(){
    console.log("ms clientes : http://localhost:"+config.ms_pedidos.port);
})
