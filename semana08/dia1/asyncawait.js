/*
async function funcion_asincrona(){
    return 100;
}

const valorasincrono = await funcion_asincrona();

funcion_asincrona().then(value=>{
    console.log("el resultado devuelto es : ",value);
})
*/
async function hola(nombre){
    return new Promise(function(resolve,reject){
        setTimeout(function(){
            console.log('Hola ' + nombre);
            resolve(nombre)
            reject('hay un error');
        },500)
    })
}

async function hablar(nombre){
    return new Promise((res,rej) =>{
        setTimeout(function(){
            console.log('como te va ' + nombre);
            res(nombre);
            rej('no te entiendo')
        },500)
    })
}

async function adios(nombre){
    console.log('Adios ' + nombre);
}

async function main(){
    let nombre = await hola('César');
    await hablar(nombre);
    await adios(nombre);
}

main();