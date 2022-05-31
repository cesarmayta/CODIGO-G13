//TRABAJANDO CON EL SISTEMA OPERATIVO
const os = require('os');

console.log("arquitectura de procesador : " + os.arch());
console.log("sistema operativo : " + os.platform());
console.log("CPU :" + os.cpus().length);
console.log("Memoria RAM : " + os.totalmem());

/*utilizando async await o promesas 
mostrar la cantidad de memoria ram de tu pc en MB,KB,GB
1 kb = 1024 Bytes
1 mb = 1024 kb
1 gb = 1024 mb

1 kb = 1024 bytes
?  kb = os.totalmen()
*/
const tam = 1024;
/*kb = os.totalmem() / tam;
mb = kb / tam;
gb = mb / tam;
console.log("KB : " + kb.toFixed(2));
console.log("MB : " + mb.toFixed(2));
console.log("GB : " + gb.toFixed(2));*/

//utilizando promesas
function memoria(capacidad,tipo){
    return new Promise((resolve,reject)=>{
        let memoria_convertida = capacidad / tam;
        console.log('MEMORIA EN ' + tipo + " : " + memoria_convertida.toFixed(2));
        resolve(memoria_convertida);
    })
}

console.log("MEMORIA USANDO PROMESAS : ")
memoria(os.totalmem(),'KB')
    .then((kb)=>memoria(kb,'MB'))
    .then((mb)=>memoria(mb,'GB'))
