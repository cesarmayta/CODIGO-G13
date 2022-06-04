const express = require('express');
const jwt = require('jsonwebtoken');
const UsuarioService = require('../services/usuario.service');

function authApi(app){
    const router = express.Router();
    app.use("/auth",router);

    objUsuarioService = new UsuarioService();

    router.post("/",async function(req,res){
        const {body: usuario} = req;
        console.log("paso 1 ) data enviado por post : \n " + usuario.usuario + " - " + usuario.password)
        //llamamos el servicio de usuario para validar los datos
        const dataValidate = await objUsuarioService.validate({usuario});
        console.log("data validada : " + dataValidate.id)
        if(dataValidate.id > 0){
            const token = jwt.sign(
                dataValidate,
                'codigo2022',
                {
                    expiresIn:'1h'
                }
            )
            res.status(200).json({
                status:true,
                content:token
            })
        }
        else{
            res.status(401).json({
                status:false,
                content:'usuario o clave invalidos'
            })
        }
    })
}

module.exports = authApi;