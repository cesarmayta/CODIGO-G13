function errorHandler(err,req,res,next){
    res.status(500).json({
        status:false,
        content:err.message,
        stack:err.stack
    })
}

function boomErrorHandler(err,req,res,next){
    if(err.isBoom){
        const {output} = err;
        res.status(output.statusCode).json(output.payload);
    }
}

module.exports = {errorHandler,boomErrorHandler}