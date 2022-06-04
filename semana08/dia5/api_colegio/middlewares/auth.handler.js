function verifyToken(req,res,next){
    const token = req.headers['api'];
    if(token === "qwerty123"){
        next();
    }else{
        res.status(401).json({
            message:"no esta autorizado para ingresar"
        })
    }
}

module.exports = { verifyToken }