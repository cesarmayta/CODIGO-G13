const express = require('express');
const PedidoService = require('../services/pedido.services');

function pedidoApi(app){
    const router = express.Router();
    app.use("/pedido",router);

    const objPedidoService = new PedidoService();

    router.post("/",async function(req,res){
        const {body:pedido} = req;
        console.log(pedido);

        try{
            const crearPedido = await objPedidoService.create({pedido});
            res.status(201).json({
                status:true,
                content:crearPedido
            })
        }catch(err){
            console.log(err);
        }

    })
}

module.exports = pedidoApi;