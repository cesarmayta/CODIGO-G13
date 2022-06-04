const express = require('express');
const {config} = require('./config');
const cors = require('cors');

//middlewares
const {errorHandler,boomErrorHandler} = require('./middlewares/error.handler');
const {verifyToken} = require('./middlewares/auth.handler');

//routes
const alumnoApi = require('./routes/alumno.routes');
const cursoApi = require('./routes/curso.routes');
const authApi = require('./routes/auth.routes');
const usuarioApi = require('./routes/usuario.routes');




const app = express();

app.use(cors());

app.use(express.json());

app.get('/',verifyToken,(req,res)=>{

    res.json({
        'status':true,
        'content':'servidor activo'
    })
})

alumnoApi(app);
cursoApi(app);
authApi(app);
usuarioApi(app);

//manejo de errores
app.use(boomErrorHandler);
app.use(errorHandler);

app.listen(config.port,()=>console.log('servidor en http://localhost:'+config.port));