const express = require('express');
const ClienteService = require('../services/cliente.service');

function clienteApi(app){
    const router = express.Router();
    app.use("/cliente",router);

    const objClienteService = new ClienteService();

    router.get('/',async function(req,res){
        try{
            const clientes = await objClienteService.getAll();
            res.status(200).json({
                status:true,
                content:clientes
            })
        }catch(err){
            console.log(err);
        }
    })
}

module.exports = clienteApi;