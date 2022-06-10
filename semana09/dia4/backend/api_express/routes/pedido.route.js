const express = require('express');
const PedidoService = require('../services/pedido.services');

function pedidoApi(app){
    const router = express.Router();
    app.use("/pedido",router);

    const objPedidoService = new PedidoService();

    router.get('/',async function(req,res){
        try{
            const pedidos = await objPedidoService.getAll();
            res.status(200).json({
                status:true,
                content:pedidos
            })
        }catch(err){
            console.log(err);
        }
    })

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