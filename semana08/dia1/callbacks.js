function hola(nombre,primercallback){
    setTimeout(function(){
        console.log('Hola ' + nombre);
        primercallback(nombre);
    },500);
}

function hablar(nombre,segundocallback){
    setTimeout(function(){
        console.log("como te va " + nombre);
        segundocallback(nombre);
    })
}

function adios(nombre){
    console.log("Adios " + nombre );
}


let nom = 'César';
hola(nom,function(nombre){
    hablar(nombre,function(nombre){
        adios(nombre);
    })
});
//hablar(nom);