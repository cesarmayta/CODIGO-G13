const express = require('express');
const UsuarioService = require('../services/usuario.service');

function  usuarioApi(app){
    const router = express.Router();
    app.use("/usuario",router);

    const objUsuarioService = new UsuarioService();

    router.get("/",async function(req,res){
        try{
            const data = await objUsuarioService.getAll();
            res.status(200).json({
                status:true,
                content:data
            })
        }catch(err){
            console.log(err)
        }
    })

    router.post("/",async function(req,res){
        const {body: usuario} = req;
        console.log(usuario);
        try{
            const crearUsuario = await objUsuarioService.create({usuario});
            res.status(201).json({
                status:true,
                content:crearUsuario
            })
        }catch(err){
            console.log(err);
        }
    })
}

module.exports = usuarioApi;