module.exports = {
  apps : [
    {
    name   : "apicliente",
    script : "./api_express/microservices/cliente.ms.js"
    },
    {
      name   : "apipedido",
      script : "./api_express/microservices/pedido.ms.js"
    }
  ]
}
