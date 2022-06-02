const { application } = require('express');
const express = require('express');

const app = express();

app.use(express.json());

app.get('/',(req,res)=>{
    res.json({
        'status':true,
        'content':'servidor activo'
    })
})

app.listen(5000,()=>console.log('servidor en http://localhost:5000'));