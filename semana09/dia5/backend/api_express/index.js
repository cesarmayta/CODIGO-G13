const express = require('express');
const {config} = require('./config');
const cors = require('cors');


const clienteApi = require('./routes/cliente.route');
const pedidoApi = require('./routes/pedido.route');

const app = express();

//middlewares
app.use(cors());
app.use(express.json());

//rutas
clienteApi(app);
pedidoApi(app);

app.listen(config.port,()=>console.log(`servidor http://localhost:${config.port}`));