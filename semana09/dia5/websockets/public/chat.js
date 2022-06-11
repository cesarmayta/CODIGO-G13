const socket = io('http://localhost:5000');

let output = document.getElementById('output');
let mensaje = document.getElementById('mensaje');
let btn = document.getElementById('enviar');

btn.addEventListener('click',function(){
    console.log(mensaje.value);
    socket.emit('mensajecliente',{
        mensaje:mensaje.value
    })
})

socket.on('mensajeservidor',function(data){
    console.log(data);
    output.innerHTML += `
    <div class="card">
        <div class="card-body">
             ${data.mensaje}
        </div>
    </div>
    `;
})