const express = require('express');
const {config} = require('./config');
const cors = require('cors');

const app = express();

app.set('port',config.port);

//middlewares
app.use(cors());
app.use(express.json());

app.get('/',(req,res)=>res.json({content:'api ok'}))

//rutas
app.use('/tarea',require('./routes/tarea.route'));

module.exports = app;