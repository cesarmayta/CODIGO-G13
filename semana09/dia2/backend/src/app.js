const express = require('express');
const {config} = require('./config');

const app = express();

app.set('port',config.port);

app.use(express.json());

app.get('/',(req,res)=>res.json({content:'api ok'}))

module.exports = app;