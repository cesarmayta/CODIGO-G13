const http = require('http');

http.createServer(function(req,res){
    console.log("servidor web iniciado");
    
    console.log(req.url);
    switch(req.url){
        case '/hola':
            res.write('estas en la pagina hola');
            res.end();
            break;
        default:
            res.write('<h1>bienvenido a mi sitio web con nodejs</h1>');
            res.end();
    }
}).listen(5000);