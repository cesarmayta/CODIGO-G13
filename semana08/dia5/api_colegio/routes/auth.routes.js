const express = require('express');
const jwt = require('jsonwebtoken');

function authApi(app){
    const router = express.Router();
    app.use("/auth",router);

    router.post("/",async function(req,res){
        const {usuario,password} = req.body;

        if(usuario === "admin" && password === "1234"){
            const token = jwt.sign(
                {usuario:'admin'},
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